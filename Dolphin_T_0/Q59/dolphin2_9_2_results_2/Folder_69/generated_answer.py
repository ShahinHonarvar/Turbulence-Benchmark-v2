def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and i % 10 != 0:
            trunc = i // 10
            while trunc and is_prime(trunc):
                trunc //= 10
            else:
                primes.append(i)
    return primes