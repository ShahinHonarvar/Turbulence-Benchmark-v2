def insert_after_index(lst):
    i = 0
    while i < len(lst):
        if lst[i] == 90:
            break
        i += 1
    return lst[:i + 1] + [80] + lst[i + 1:]