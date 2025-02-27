def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    else:
        sorted_nums = sorted(nums[:6])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]