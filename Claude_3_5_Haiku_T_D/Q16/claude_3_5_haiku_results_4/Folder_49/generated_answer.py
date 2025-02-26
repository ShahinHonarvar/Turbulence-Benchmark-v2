def sum_even_ints_inclusive(nums):
    if len(nums) <= 80:
        return 0
    return sum((num for num in nums[8:81] if num % 2 == 0))