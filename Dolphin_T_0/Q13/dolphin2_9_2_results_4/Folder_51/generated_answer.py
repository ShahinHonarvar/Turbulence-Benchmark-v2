def find_second_largest_num(lst):
    if 1 <= 8 < len(lst):
        sorted_nums = sorted(lst[1:9])
        return sorted_nums[-2] if len(sorted_nums) > 1 else None
    else:
        return None