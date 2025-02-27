def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    primes = []
    while num > 0:
        if is_prime(num):
            primes.append(num)
        num //= 10
    return primes

def all_right_truncatable_prime(numbers):
    limit = numbers[975]
    right_truncatable_primes_list = []
    for num in range(limit):
        primes = right_truncatable_primes(num)
        if primes and primes[-1] < limit:
            right_truncatable_primes_list.extend(primes)
    return sorted(set(right_truncatable_primes_list), reverse=True)