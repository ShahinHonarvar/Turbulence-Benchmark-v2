def find_smallest_num(nums):
    min_num = nums[1]
    for num in nums[1:6]:
        if num < min_num:
            min_num = num
    return min_num