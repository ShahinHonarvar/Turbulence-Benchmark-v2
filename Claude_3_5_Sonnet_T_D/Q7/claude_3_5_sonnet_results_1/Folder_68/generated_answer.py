def all_even_ints_inclusive(integer_list):
    result = []
    for i in range(min(9, len(integer_list))):
        if integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result