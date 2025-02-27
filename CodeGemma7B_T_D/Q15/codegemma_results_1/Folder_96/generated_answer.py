def sum_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(50, 201):
        if i % 2 != 0:
            odd_nums.append(nums[i])
    if not odd_nums:
        return 0
    return sum(odd_nums)