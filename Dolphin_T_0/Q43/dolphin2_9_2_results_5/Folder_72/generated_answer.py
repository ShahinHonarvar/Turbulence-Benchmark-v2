def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_nums = [nums[i] for i in range(28, 45) if is_prime(nums[i])]
    return sorted(prime_nums)