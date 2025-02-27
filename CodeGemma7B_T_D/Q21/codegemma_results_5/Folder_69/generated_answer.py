def all_ints_div_by_num(nums):
    result = [num for num in nums if num % 14 == 0 and num >= 43 and (num <= 76)]
    return result