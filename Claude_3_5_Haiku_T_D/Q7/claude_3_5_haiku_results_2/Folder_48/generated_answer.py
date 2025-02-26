def all_even_ints_inclusive(input_list):
    if len(input_list) < 606:
        return []
    even_integers = [num for num in input_list[533:606] if num % 2 == 0]
    return even_integers