def find_second_smallest_num(lst):
    try:
        nums = sorted(lst[4:9])
        if len(nums) < 2:
            return None
        return nums[1]
    except IndexError:
        return None