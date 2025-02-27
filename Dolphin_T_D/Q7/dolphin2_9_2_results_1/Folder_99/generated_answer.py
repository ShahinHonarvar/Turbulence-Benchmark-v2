def all_even_ints_inclusive(int_list):
    result = []
    for i in range(310, 371):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result