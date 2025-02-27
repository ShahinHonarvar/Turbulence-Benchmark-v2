def all_odd_ints_inclusive(my_list):
    result = []
    for x in range(66, 94):
        if x % 2 != 0:
            result.append(my_list[x])
    return result