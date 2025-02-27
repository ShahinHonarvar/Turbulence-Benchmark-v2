def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    return sorted(nums[1:9])[1]