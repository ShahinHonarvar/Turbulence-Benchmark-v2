def all_ints_div_by_num(nums):
    return [num for num in nums if num % 5 == 0 and num in range(len(nums))]