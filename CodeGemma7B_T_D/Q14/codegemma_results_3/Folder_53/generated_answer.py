def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 2:
        return None
    for i in range(1, 100):
        if i >= len(nums):
            return None
        if nums[i] == nums[i - 1]:
            continue
        return nums[i]