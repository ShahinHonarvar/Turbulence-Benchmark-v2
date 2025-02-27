def find_second_smallest_num(lst):
    start = 17
    end = 78
    if end - start > 0:
        subset = sorted(lst[start:end + 1])
        if len(subset) > 2:
            return subset[1]
    return None