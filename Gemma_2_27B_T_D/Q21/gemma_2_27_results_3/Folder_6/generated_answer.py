def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 13 <= i <= 63 and num % 46 == 0]