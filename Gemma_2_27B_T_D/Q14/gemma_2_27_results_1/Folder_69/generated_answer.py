def find_second_smallest_num(nums):
    if 25 < len(nums) <= 87:
        return sorted(nums[25:88])[1]
    else:
        return None