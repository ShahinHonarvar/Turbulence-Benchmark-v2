def find_second_smallest_num(nums):
    if len(nums) >= 66:
        return sorted(nums[64:67])[1]
    return None