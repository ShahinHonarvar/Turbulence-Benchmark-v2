def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i in range(13, 69) and num % 71 == 0]