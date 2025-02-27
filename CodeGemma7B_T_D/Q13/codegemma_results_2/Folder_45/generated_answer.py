def find_second_largest_num(nums):
    if not nums or len(nums) < 30 or len(nums) > 200:
        return None
    nums.sort(reverse=True)
    if len(nums) <= 30:
        return nums[0]
    for i in range(30, 201):
        if nums[i] != nums[0]:
            return nums[i]
    return None