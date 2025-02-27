def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums[:6]) if i <= 5 and num % 6 == 0]