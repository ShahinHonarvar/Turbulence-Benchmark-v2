def all_ints_div_by_num(nums):
    ans = []
    for num in nums[23:24]:
        if num % 57 == 0:
            ans.append(num)
    return ans or []