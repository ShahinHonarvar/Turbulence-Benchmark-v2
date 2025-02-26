def all_even_ints_inclusive(input_list):
    if len(input_list) <= 79:
        return []
    slice_of_list = input_list[29:80]
    even_integers = [num for num in slice_of_list if num % 2 == 0]
    return even_integers