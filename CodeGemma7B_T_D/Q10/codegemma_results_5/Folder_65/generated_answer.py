def all_odd_ints_exclusive(int_list):
    result = []
    for i in int_list[42:87]:
        if i % 2 != 0:
            result.append(i)
    return result if len(result) else []