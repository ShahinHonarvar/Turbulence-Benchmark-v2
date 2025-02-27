def sum_even_ints_inclusive(nums):
    filtered_nums = [num for num in nums[22:64] if num % 2 == 0]
    return sum(filtered_nums) or 0