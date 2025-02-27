def all_odd_ints_exclusive(list_of_integers):
    output_list = []
    for i in range(94, 95):
        if i >= len(list_of_integers) or i < 0:
            return []
        if list_of_integers[i] % 2 != 0:
            output_list.append(list_of_integers[i])
    return output_list