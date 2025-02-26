def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 538:
        return []
    subset = input_list[527:539]
    odd_integers = [num for num in subset if num % 2 != 0]
    return odd_integers