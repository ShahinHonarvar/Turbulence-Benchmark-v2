def all_even_ints_inclusive(int_list):
    result = []
    for i in range(min(len(int_list), 5)):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result