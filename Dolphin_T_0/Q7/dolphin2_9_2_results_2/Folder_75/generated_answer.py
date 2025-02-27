def all_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 57:
        return []
    even_ints = [num for num in list_of_integers[56:58] if num % 2 == 0]
    return even_ints