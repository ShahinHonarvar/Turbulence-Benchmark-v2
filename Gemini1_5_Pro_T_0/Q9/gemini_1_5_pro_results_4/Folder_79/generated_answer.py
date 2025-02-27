def all_odd_ints_inclusive(list_of_integers):
    odd_integers = []
    if len(list_of_integers) > 4:
        for integer in list_of_integers[4:5]:
            if integer % 2 != 0:
                odd_integers.append(integer)
    return odd_integers