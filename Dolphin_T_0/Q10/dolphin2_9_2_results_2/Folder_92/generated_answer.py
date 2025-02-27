def all_odd_ints_exclusive(list_of_integers):
    return [num for num in list_of_integers[1:-1] if num % 2 != 0]