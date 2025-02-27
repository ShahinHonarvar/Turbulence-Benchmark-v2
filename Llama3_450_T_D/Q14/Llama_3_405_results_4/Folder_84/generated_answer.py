def find_second_smallest_num(nums):
    sliced_nums = sorted(nums[40:81])
    if len(sliced_nums) < 2:
        return None
    else:
        return sliced_nums[1]