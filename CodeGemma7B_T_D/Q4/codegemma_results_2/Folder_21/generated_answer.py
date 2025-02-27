def all_pos_ints_exclusive(nums):
    ans = []
    for num in nums[743:867]:
        if num > 0:
            ans.append(num)
    return ans