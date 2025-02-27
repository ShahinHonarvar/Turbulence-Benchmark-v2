def find_second_smallest_num(nums):
    if len(nums[1:9]) >= 2:
        return sorted(nums[1:9])[1]
    return None