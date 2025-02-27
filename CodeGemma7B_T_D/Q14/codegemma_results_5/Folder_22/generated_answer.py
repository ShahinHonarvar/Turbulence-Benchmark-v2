def find_second_smallest_num(nums):
    if len(nums) == 0 or len(nums) < 40 or len(nums) > 200:
        return None
    nums.sort()
    if nums[39] >= nums[-1]:
        return None
    for i in range(40, 201):
        if nums[40] < nums[i] < nums[-1]:
            return nums[i]
    return None