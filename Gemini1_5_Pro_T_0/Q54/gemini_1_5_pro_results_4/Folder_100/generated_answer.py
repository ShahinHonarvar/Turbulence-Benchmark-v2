def all_right_truncatable_prime(nums):
    x = nums[26]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        for i in range(len(str(num)) - 1, 0, -1):
            if int(str(num)[:i]) not in primes:
                return False
        return True
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
        if is_right_truncatable_prime(prime):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)