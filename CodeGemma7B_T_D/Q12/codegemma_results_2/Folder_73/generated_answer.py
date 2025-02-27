def find_smallest_num(nums):
    smallest_num = float('inf')
    for i in range(55, 99):
        if nums[i] < smallest_num:
            smallest_num = nums[i]
    return smallest_num