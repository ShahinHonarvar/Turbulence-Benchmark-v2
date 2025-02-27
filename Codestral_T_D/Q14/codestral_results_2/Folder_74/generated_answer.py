def find_second_smallest_num(lst):
    subset = lst[36:47]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    second_smallest = min(subset)
    return second_smallest