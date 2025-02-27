def return_nth_smallest_ascii(input_string):
    filtered_chars = sorted(input_string[22:75])
    n = 12
    for char in filtered_chars:
        if filtered_chars.index(char) == n - 1:
            return char