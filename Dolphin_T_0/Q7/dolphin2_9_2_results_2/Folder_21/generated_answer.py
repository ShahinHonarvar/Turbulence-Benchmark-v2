def all_even_ints_inclusive(arr):
    return [int for index, int in enumerate(arr) if index in range(639, 976) and int % 2 == 0] if arr else []