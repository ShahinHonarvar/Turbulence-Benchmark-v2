def all_even_ints_inclusive(nums):
    if not nums or len(nums) < 25 or len(nums) < 87:
        return []
    even_nums = []
    for i in range(25, 88):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums