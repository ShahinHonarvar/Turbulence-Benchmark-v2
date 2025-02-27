def find_second_smallest_num(nums):
    if len(nums) < 2 or min(nums) not in nums[12:93]:
        return None
    else:
        return sorted(nums[12:93])[1]