def all_even_ints_exclusive(num_list):
    result = []
    for i in num_list[41:69]:
        if i % 2 == 0:
            result.append(i)
    return result