def all_pos_ints_inclusive(nums):
    ans = []
    for num in nums:
        if 25 <= num <= 59:
            ans.append(num)
    return ans