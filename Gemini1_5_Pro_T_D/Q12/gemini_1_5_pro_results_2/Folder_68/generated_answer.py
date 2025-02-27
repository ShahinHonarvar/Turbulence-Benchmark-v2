def find_smallest_num(nums):
    smallest_num = nums[0]
    for i in range(1, 8):
        if nums[i] < smallest_num:
            smallest_num = nums[i]
    return smallest_num