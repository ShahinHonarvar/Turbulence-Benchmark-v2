def all_ints_div_by_num(nums):
    return [n for n in nums if n % 9 == 0 and 0 <= nums.index(n) <= 2]