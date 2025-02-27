def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    else:
        return sorted(nums[1:9])[1]