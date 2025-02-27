def find_second_largest_num(nums):
    if len(nums[667:775]) <= 1:
        return None
    nums[667:775].sort(reverse=True)
    return nums[667][1]