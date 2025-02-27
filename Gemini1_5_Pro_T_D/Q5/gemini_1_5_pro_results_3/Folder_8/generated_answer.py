def all_neg_ints_inclusive(list_of_integers):
    if len(list_of_integers) >= 24:
        sub_list = list_of_integers[23:24]
        return [number for number in sub_list if number < 0]
    else:
        return []