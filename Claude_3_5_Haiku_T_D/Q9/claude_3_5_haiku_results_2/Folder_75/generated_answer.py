def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 57:
        return []
    odd_ints = [num for num in input_list[56:58] if num % 2 != 0]
    return odd_ints