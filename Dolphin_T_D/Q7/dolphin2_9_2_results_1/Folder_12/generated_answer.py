def all_even_ints_inclusive(input_list):
    even_ints = [num for num in input_list[14:65] if num % 2 == 0]
    if not even_ints:
        even_ints = []
    return even_ints