def all_ints_div_by_both_two_nums(nums):
    ans = []
    for num in nums[72:94]:
        if num % 32 == 0 and num % 44 == 0:
            ans.append(num)
    return ans