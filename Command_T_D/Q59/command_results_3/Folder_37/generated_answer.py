def all_left_truncatable_prime(nums):
    return [str(i) for i in sorted(nums, reverse=True) if str(i) in str(nums[35])][-1]