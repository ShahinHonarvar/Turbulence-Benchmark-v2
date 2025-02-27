def all_odd_ints_exclusive(integer_list):
    odd_ints = []
    for index in range(1, 3):
        if len(integer_list) > index and isinstance(integer_list[index], int) and (integer_list[index] % 2 != 0):
            odd_ints.append(integer_list[index])
    return odd_ints