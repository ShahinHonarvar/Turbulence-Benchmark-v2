def all_odd_ints_inclusive(nums):
    new_list = []
    if 22 in nums and 88 in nums:
        for i in range(nums.index(22), nums.index(88) + 1):
            if nums[i] % 2 != 0:
                new_list.append(nums[i])
    return new_list