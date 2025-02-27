def find_second_smallest_num(lst):
    try:
        selected_nums = sorted(lst[31:35])
        return selected_nums[1]
    except IndexError:
        return None