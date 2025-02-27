def all_odd_ints_inclusive(num_list):
    result = []
    for i in range(1, 9):
        if i % 2 != 0:
            if i in num_list:
                result.append(i)
    return result