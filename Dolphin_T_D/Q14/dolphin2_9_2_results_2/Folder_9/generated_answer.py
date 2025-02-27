def find_second_smallest_num(lst):
    if not lst[70:200]:
        return None
    min_1 = min(lst[70:200])
    min_2 = min((x for x in lst[70:200] if x != min_1))
    return min_2 if min_2 else None