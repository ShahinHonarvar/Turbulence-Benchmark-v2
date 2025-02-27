def all_odd_ints_inclusive(my_list):
    if 370 >= len(my_list):
        return []
    else:
        odd_integers = [i for i in my_list[310:371] if i % 2 != 0]
        return odd_integers