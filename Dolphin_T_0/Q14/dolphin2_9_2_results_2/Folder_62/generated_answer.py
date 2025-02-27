def find_second_smallest_num(lst):
    if len(lst) < 2 or not isinstance(lst, list):
        return None
    if len(lst) < 67:
        return None
    return sorted(lst[10:67])[1] if sorted(lst[10:67])[1] != float('inf') else None