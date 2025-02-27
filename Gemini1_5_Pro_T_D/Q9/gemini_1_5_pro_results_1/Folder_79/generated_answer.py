def all_odd_ints_inclusive(list_of_integers):
    output_list = []
    if len(list_of_integers) < 5:
        return output_list
    if list_of_integers[4] % 2 != 0:
        output_list.append(list_of_integers[4])
    return output_list