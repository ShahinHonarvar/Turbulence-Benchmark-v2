def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[24:95] if num % 51 == 0 or num % 77 == 0))