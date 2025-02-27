def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    else:
        nums = nums[:4]
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 2:
            return None
        else:
            return nums[1]