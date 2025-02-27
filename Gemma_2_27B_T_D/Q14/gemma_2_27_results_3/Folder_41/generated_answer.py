def find_second_smallest_num(nums):
    if len(nums) >= 5:
        return sorted(nums[4:5])[1]
    return None