def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[84]
    truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            m = n
            while m > 1:
                m //= 10
                if not is_prime(m):
                    break
            else:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)