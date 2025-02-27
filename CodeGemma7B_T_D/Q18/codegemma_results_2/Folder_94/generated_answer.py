def sum_ints_div_by_either_nums(nums):
    ans = 0
    for num in nums[93:95 + 1]:
        if num % 53 == 0 or num % 91 == 0:
            ans += num
    return ans if ans else 0