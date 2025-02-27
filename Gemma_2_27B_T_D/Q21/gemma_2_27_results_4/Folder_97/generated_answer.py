def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 17 and i <= 63 and (num % 89 == 0)]