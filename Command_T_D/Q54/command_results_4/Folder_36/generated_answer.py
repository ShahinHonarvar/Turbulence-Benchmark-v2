def all_right_truncatable_prime(nums):
    return sorted((nums for num in nums if all((nums[i] % 10 != d for i in range(len(nums) - 1) for d in range(10)))))