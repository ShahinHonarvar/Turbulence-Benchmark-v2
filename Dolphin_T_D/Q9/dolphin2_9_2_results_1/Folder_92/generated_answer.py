def all_odd_ints_inclusive(nums):
    odd_nums = []
    if nums[0] % 2 != 0:
        odd_nums.append(nums[0])
    if nums[1] % 2 != 0:
        odd_nums.append(nums[1])
    return odd_nums