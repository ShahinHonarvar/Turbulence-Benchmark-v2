def all_pos_ints_inclusive(list):
    results = []
    for i in range(25, 88):
        if list[i] > 0:
            results.append(list[i])
    return results if results else []