def find_second_smallest_num(lst):
    try:
        nums = sorted(set(lst[80:201]))
        return nums[1] if len(nums) > 1 else None
    except IndexError:
        return None