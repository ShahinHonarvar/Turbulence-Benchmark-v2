from functools import reduce

def sum_ints_div_by_either_nums(nums):
    filtered = [num for num in nums[0:10] if num % 6 == 0 or num % -3 == 0]
    return reduce(lambda result, num: result + num, filtered, 0) if filtered else 0