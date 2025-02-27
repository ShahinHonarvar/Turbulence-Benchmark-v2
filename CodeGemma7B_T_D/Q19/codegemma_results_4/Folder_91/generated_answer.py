def all_ints_not_div_by_num(nums):
    return [num for num in nums if num % 8 != 0 and num > 0 and (0 <= nums.index(num) <= 4)]