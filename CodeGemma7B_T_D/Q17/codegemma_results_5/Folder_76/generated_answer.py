def all_ints_div_by_both_two_nums(nums):
    ans = [num for num in nums[250:629 + 1] if num % 850 == 0 and num % 587 == 0]
    return ans if ans else []