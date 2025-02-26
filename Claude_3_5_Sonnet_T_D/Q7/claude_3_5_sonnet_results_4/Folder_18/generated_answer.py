def all_even_ints_inclusive(integer_list):
    result = []
    for i in range(35, 50):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result