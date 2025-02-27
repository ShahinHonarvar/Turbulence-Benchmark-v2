def find_primes_between_indices(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([nums[i] for i in range(len(nums)) if i >= 167 and i <= 785 and is_prime(nums[i])], reverse=True)