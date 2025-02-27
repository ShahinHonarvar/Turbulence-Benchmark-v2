def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    return sorted([n for n in nums[61:80] if is_prime(n)])