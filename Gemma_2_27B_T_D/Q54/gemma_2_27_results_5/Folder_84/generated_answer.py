def all_right_truncatable_prime(nums):
    x = nums[630]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        right_truncatable = True
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[:-i])):
                right_truncatable = False
                break
        if right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True