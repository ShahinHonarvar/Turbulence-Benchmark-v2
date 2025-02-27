def sum_even_ints_inclusive(nums):
    return sum(nums[70:201][::2]) if len(nums[70:201][::2]) > 0 else 0