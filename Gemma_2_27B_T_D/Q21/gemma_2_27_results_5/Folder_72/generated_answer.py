def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 11 and i <= 82 and (num % -47 == 0)]