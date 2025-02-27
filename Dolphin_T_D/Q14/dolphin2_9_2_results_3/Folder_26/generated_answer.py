def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    mid_nums = nums[62:79]
    if len(mid_nums) != 16:
        return None
    mid_nums.sort()
    for i in range(1, len(mid_nums)):
        if not mid_nums[i] == mid_nums[i - 1]:
            return mid_nums[i]
    return None