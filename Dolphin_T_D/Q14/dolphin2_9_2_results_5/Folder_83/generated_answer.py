def find_second_smallest_num(nums):
    if 90 <= 200 < len(nums):
        return sorted(nums[90:201])[1]
    else:
        return None