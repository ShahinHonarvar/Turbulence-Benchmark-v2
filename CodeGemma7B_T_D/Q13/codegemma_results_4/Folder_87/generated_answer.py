def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums[36:47]) > 1:
        return nums[37]
    else:
        return None