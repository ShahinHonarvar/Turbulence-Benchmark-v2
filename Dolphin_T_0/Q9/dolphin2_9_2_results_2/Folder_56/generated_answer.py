def all_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd_nums.append(nums[i])
    return odd_nums