def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % 6 != 0 and 3 < nums.index(num) < 9]