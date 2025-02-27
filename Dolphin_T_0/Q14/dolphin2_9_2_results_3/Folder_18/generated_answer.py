def find_second_smallest_num(lst):
    if 30 <= len(lst) < 48:
        section = lst[30:48]
        if len(section) < 2:
            return None
        else:
            min_val = min(section)
            section.remove(min_val)
            return min(section) if len(section) >= 1 else None
    else:
        return None