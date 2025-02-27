def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums[75:95] if num % 2 == 0]
    return sum(even_nums) or 0