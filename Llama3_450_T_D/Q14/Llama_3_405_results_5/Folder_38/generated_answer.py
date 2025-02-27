def find_second_smallest_num(lst):
    try:
        nums = sorted(lst[37:52])
        if len(nums) < 2:
            return None
        else:
            return nums[1]
    except IndexError:
        return None