def all_even_ints_exclusive(list_of_ints):
    if list_of_ints[20:200] == []:
        return []
    else:
        return list(filter(lambda x: x % 2 == 0, list_of_ints))[20:200]