def find_second_smallest_num(nums):
    if len(nums[42:69]) < 2:
        return None
    els = sorted(nums[42:69])
    return els[1]