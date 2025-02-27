def find_smallest_num(lst):
    if len(lst) < 200:
        return None
    subset = lst[100:201]
    return min(subset)