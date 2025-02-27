def all_pos_ints_inclusive(nums):
    ans = []
    for num in nums[75:89]:
        if num > 0:
            ans.append(num)
    return ans if ans else []