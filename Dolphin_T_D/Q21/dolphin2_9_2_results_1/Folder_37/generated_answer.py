def all_ints_div_by_num(nums):
    result = [num for num in nums if num % 3 == 0]
    return result[4:5] if 4 < len(result) else []