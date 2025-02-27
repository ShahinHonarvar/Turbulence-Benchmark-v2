def find_second_largest_num(l):
    if len(l) < 2:
        return None
    first_max_value = max(l[:7])
    l.remove(first_max_value)
    if not l:
        return None
    return max(l[:7])