def find_second_smallest_num(lst):
    try:
        nums = sorted(lst[31:73])
        if len(nums) < 2:
            return None
        else:
            return nums[1]
    except IndexError:
        return None