def all_even_ints_inclusive(num_list):
    if len(num_list) <= 92:
        return []
    subset = num_list[62:93]
    return [num for num in subset if num % 2 == 0]