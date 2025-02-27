def find_second_smallest_num(nums):
    if len(nums) < 66 or len(nums) < 65:
        return None
    else:
        return sorted(nums[64:67])[1]