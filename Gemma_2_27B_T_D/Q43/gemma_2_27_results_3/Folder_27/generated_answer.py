def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_nums = []
    if 11 <= len(nums) and 11 <= len(nums):
        for i in range(11, 12):
            if is_prime(nums[i]):
                prime_nums.append(nums[i])
    return sorted(prime_nums)