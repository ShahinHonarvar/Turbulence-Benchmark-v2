def all_even_ints_exclusive(nums):
    ans = []
    for i in range(38, 52):
        if nums[i] % 2 == 0:
            ans.append(nums[i])
    return ans