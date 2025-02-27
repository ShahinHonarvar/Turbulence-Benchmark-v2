def find_second_smallest_num(nums):
    if 75 <= len(nums) <= 94:
        nums = sorted(nums[75:95])
        if len(nums) > 1:
            return nums[1]
        else:
            return None
    else:
        return None