def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    primes = []
    for num in range(x):
        if is_prime(num):
            k = num
            while k != 0:
                if not is_prime(k):
                    break
                k //= 10
                if k == 0:
                    primes.append(num)
    return sorted(primes)