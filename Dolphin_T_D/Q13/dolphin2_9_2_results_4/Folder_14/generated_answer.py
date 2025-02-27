def find_second_largest_num(nums):
    nums = nums[4:8]
    nums = list(set(nums))
    nums.sort(reverse=True)
    if len(nums) >= 2:
        return nums[1]
    else:
        return None