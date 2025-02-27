def find_second_largest_num(nums):
    if len(nums[70:85]) < 2:
        return None
    return sorted(nums[70:85])[-2]