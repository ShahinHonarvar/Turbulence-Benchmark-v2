def all_even_ints_exclusive(int_list):
    if len(int_list) < 35:
        return []
    result = []
    for i in int_list[27:34]:
        if i % 2 == 0:
            result.append(i)
    return result