def all_pos_ints_exclusive(list):
    if list[36:52] == [i for i in list[36:52] if i > 0 and i < 53]:
        return [num + 1 for num in range(36, 52, 1)]
    else:
        return []