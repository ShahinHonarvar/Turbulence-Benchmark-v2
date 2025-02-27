def find_second_smallest_num(lst):
    try:
        target_slice = sorted(lst[31:35])
        if len(target_slice) < 2:
            return None
        return target_slice[1]
    except IndexError:
        return None