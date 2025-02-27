def all_ints_div_by_both_two_nums(nums):
    ans = [n for n in nums[44:60] if n % 39 == 0 and n % 15 == 0]
    return ans if ans else []