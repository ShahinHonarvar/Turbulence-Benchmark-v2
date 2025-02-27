def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[80:201] if num % 10 == 0 and num % 1000 == 0]
    return result