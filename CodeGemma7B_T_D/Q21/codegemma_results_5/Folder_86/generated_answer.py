def all_ints_div_by_num(nums):
    ans = []
    for num in nums[44:74]:
        if num % 88 == 0:
            ans.append(num)
    return ans if ans else []