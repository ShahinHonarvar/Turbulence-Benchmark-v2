def all_even_ints_inclusive(integer_list):
    if len(integer_list) < 606:
        return []
    result = []
    for i in range(533, 606):
        if integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result