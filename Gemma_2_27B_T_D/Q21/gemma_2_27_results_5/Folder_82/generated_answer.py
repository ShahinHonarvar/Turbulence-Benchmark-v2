def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums[:3]) if i < 3 and num % 3 == 0]