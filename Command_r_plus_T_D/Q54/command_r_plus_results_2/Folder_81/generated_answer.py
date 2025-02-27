def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(10):
        num = n * 10 + i
        if is_prime(num):
            primes.append(num)
    return primes

def all_right_truncatable_prime(numbers):
    limit = numbers[98]
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            truncatable_primes = [i]
            num = i
            while num > 9:
                num //= 10
                if is_prime(num):
                    truncatable_primes.append(num)
                else:
                    break
            if len(truncatable_primes) == len(str(i)):
                primes.extend(truncatable_primes)
    return sorted(primes)