def all_even_ints_inclusive(input_list):
    if len(input_list) <= 605:
        return []
    even_nums = [num for num in input_list[533:606] if num % 2 == 0]
    return even_nums