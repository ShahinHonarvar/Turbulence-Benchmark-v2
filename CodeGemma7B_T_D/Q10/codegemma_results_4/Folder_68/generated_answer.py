def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(9):
        if i % 2 != 0 and i not in int_list:
            result.append(i)
    return result