def all_odd_ints_inclusive(int_list):
    result = []
    for i in range(len(int_list)):
        if int_list[i] % 2 != 0 and (i <= 7 and i >= 0):
            result.append(int_list[i])
    return result