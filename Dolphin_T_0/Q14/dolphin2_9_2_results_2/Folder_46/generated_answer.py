def find_second_smallest_num(nums):
    if 13 <= 68 < len(nums):
        num_set = nums[13:69]
        num_set.sort()
        if len(num_set) > 1:
            return num_set[1]
        else:
            return None
    else:
        return None