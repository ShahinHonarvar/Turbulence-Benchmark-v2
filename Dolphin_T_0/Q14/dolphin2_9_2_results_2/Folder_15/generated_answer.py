def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    else:
        nums = nums[:4]
        nums_set = set(nums)
        min_num = min(nums_set)
        nums_set.remove(min_num)
        if len(nums_set) < 1:
            return None
        else:
            return min(nums_set)