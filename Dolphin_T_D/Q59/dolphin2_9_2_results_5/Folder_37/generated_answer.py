def all_left_truncatable_prime(numbers):
    primes = []
    x = numbers[35]
    for num in range(2, x):
        if is_prime(num):
            n = num
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True