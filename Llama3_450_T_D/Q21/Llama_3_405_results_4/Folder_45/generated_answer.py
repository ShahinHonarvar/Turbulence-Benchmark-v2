def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i <= 2 and num % 9 == 0]