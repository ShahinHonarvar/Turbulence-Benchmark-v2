def all_ints_not_div_by_num(nums):
    return [num for num in nums if num not in range(10, 100) or num % 100 != 0]