def find_second_largest_num(nums):
    if 200 in range(len(nums)) and len(nums) > 201:
        return sorted(nums[200:201])[1]
    return None