def all_odd_ints_inclusive(input_list):
    if len(input_list) < 99:
        return []
    odd_integers = [num for num in input_list[55:99] if num % 2 != 0]
    return odd_integers