def all_ints_not_div_by_num(nums):
    return [num for index, num in enumerate(nums) if index >= 70 and index < 98 and (num % -88 != 0)]