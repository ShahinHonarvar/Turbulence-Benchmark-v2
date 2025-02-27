def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 10 and i <= 37 and (num % -64 == 0)]