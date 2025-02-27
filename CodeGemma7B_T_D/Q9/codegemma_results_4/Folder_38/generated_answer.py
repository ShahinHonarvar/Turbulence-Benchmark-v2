def all_odd_ints_inclusive(nums):
    odd_nums = []
    for i in nums[22:64]:
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums