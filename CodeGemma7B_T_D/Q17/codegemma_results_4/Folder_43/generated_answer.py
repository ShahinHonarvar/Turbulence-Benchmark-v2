def all_ints_div_by_both_two_nums(nums):
    ans = []
    for num in nums[57:86]:
        if num % -77 * num % -32 == 0:
            ans.append(num)
    return ans