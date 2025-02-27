def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    else:
        sorted_nums = sorted(nums[:6])
        if len(sorted_nums) == len(set(sorted_nums)):
            return sorted_nums[1]
        else:
            return None