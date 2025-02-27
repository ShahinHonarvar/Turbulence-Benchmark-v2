def find_second_smallest_num(lst):
    filtered = [x for x in lst[20:201] if x is not None] if lst else []
    if len(filtered) < 2 or filtered[0] == filtered[1]:
        return None
    for i in range(2, len(filtered)):
        if filtered[i] not in [filtered[0], filtered[1]]:
            return filtered[i]
    return None