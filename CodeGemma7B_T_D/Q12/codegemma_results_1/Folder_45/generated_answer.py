def find_smallest_num(nums):
    smallest_num = float('inf')
    for num in nums[30:201]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num