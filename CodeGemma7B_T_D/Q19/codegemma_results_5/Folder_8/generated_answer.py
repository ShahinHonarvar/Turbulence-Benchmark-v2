def all_ints_not_div_by_num(nums):
    ans = [num for num in nums[17:88] if num % -75 != 0]
    return ans if ans else []