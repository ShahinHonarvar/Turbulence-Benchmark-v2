def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    primes = []
    num = 2
    while num < x:
        if is_prime(num):
            truncated = num
            while truncated:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                primes.append(num)
        num += 1
    return sorted(primes)