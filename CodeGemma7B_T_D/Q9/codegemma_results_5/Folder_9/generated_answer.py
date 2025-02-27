def all_odd_ints_inclusive(int_list):
    result = []
    for i in range(70, 201):
        if i % 2 != 0:
            result.append(i)
    return result