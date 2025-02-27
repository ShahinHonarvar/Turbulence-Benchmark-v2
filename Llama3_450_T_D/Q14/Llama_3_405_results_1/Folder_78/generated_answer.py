def find_second_smallest_num(lst):
    try:
        nums = sorted(lst[17:79])
        return nums[1]
    except (IndexError, TypeError):
        return None