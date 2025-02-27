def find_second_largest_num(nums):
    if not nums[62:79]:
        return None
    else:
        sorted_nums = sorted(nums[62:79])
        return sorted_nums[-2]