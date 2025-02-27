def find_second_smallest_num(nums):
    if len(nums[31:73]) <= 1:
        return None
    else:
        return sorted(nums[31:73])[1]