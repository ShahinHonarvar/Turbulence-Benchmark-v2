def sum_odd_ints_inclusive(nums):
    if len(nums) <= 30:
        return 0
    end_index = min(200 + 1, len(nums))
    odd_sum = sum((num for num in nums[30:end_index] if num % 2 != 0))
    return odd_sum