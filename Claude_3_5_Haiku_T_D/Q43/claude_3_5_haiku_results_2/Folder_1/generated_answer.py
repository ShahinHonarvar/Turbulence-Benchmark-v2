def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(nums) < 90:
        return []
    primes = [num for num in nums[87:90] if is_prime(num)]
    return sorted(primes)