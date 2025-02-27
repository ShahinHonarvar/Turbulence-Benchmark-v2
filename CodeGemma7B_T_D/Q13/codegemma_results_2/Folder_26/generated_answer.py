def find_second_largest_num(nums):
    if len(nums) < 63 or len(nums) > 100:
        return None
    nums.sort(reverse=True)
    for i in range(62, 100):
        if i < len(nums):
            return nums[i]
    return None