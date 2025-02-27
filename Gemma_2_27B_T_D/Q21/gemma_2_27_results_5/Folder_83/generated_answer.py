def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i in range(40, 401) and num % 7 == 0]