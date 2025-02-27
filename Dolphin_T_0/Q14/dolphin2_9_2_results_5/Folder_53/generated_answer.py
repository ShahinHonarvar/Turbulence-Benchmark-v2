def find_second_smallest_num(nums):
    if not nums:
        return None
    elif len(nums) < 100 or min(nums[1:101]) == float('inf'):
        return None
    else:
        return sorted(nums[1:101])[1]