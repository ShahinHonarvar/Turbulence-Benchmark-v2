def all_ints_not_div_by_num(nums):
    return [num for num in nums if num not in range(20, 200) and num % 200 != 0]