def all_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(40, 81):
        if i in nums:
            if i % 2 != 0:
                odd_nums.append(i)
    return odd_nums