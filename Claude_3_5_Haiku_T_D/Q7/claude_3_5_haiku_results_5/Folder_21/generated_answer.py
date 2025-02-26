def all_even_ints_inclusive(input_list):
    if len(input_list) <= 975:
        return []
    return [num for num in input_list[639:976] if num % 2 == 0]