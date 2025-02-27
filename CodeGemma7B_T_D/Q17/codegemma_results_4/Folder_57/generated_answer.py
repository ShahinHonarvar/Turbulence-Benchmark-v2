def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums if num % -90 == 0 and num % -59 == 0 and (51 <= nums.index(num) <= 76)]