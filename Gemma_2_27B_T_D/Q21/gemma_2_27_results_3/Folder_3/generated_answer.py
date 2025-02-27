def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 25 and i <= 59 and (num % -26 == 0)]