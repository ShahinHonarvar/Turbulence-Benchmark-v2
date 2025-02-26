def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 55:
        return []
    odd_integers = [num for num in input_list[27:56] if num % 2 != 0]
    return odd_integers