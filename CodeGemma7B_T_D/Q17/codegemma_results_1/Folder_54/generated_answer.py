def all_ints_div_by_both_two_nums(list_of_ints):
    if not list_of_ints or len(list_of_ints) < 13 or len(list_of_ints) > 91:
        return []
    result = []
    for i in range(13, 92):
        if list_of_ints[i] % -65 == 0 and list_of_ints[i] % -62 == 0:
            result.append(list_of_ints[i])
    return result