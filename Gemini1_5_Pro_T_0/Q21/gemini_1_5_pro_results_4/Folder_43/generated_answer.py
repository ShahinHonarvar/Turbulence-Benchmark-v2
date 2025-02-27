def all_ints_div_by_num(list_of_ints):
    result = []
    for i in range(max(10, len(list_of_ints))):
        if i >= len(list_of_ints) or i > 37:
            break
        if list_of_ints[i] % -64 == 0:
            result.append(list_of_ints[i])
    return result