def find_second_smallest_num(nums):
    if len(nums[31:35]) < 2:
        return None
    return sorted(nums[31:35])[1]