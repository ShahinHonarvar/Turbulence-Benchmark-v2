def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % 10 != 0 and 0 <= num < 10]