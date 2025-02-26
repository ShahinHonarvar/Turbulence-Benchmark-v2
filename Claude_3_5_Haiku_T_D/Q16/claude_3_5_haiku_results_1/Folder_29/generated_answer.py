def sum_even_ints_inclusive(nums):
    if len(nums) < 98:
        return 0
    even_sum = sum((num for num in nums[59:98] if num % 2 == 0))
    return even_sum