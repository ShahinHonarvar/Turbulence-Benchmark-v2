def all_ints_div_by_both_two_nums(nums):
    ans = []
    for num in nums[0:2 + 1]:
        if num % 6 == 0 and num % 4 == 0:
            ans.append(num)
    return ans