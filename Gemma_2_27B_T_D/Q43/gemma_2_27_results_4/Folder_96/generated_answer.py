def find_primes_between_indices(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for num in nums[31:68] if is_prime(num)]
    return sorted(primes, reverse=True)