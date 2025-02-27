def find_second_smallest_num(nums):
    nums.sort()
    for i in range(608, 610):
        if i < len(nums):
            return nums[i]
    return 'None'