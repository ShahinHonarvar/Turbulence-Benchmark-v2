def find_second_smallest_num(nums):
    target = nums[5:9]
    if len(target) < 2:
        return None
    return sorted(target)[1]