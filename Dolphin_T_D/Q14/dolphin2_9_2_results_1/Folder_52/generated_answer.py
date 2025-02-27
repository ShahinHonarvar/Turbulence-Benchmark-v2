def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    segment = lst[64:67]
    sorted_segment = sorted(segment)
    return sorted_segment[1] if len(set(segment)) == 3 else None