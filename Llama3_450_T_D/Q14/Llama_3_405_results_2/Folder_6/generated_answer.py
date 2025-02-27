def find_second_smallest_num(nums):
    if len(nums) < 80 or len(set(nums[29:80])) < 2:
        return None
    return sorted(set(nums[29:80]))[1]