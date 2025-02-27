def find_second_smallest_num(nums):
    if len(nums) >= 9:
        return sorted(nums[6:9])[1]
    return None