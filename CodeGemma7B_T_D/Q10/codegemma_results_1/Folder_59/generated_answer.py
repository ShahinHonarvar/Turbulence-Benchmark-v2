def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(10):
        if i % 2 != 0 and i not in nums:
            odd_nums.append(i)
    return odd_nums