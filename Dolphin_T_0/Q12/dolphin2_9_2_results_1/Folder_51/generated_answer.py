def find_smallest_num(lst):
    if len(lst) < 6:
        return 'Error: List does not contain enough elements.'
    return min(lst[5:7])