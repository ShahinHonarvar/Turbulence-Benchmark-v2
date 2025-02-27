def return_nth_smallest_ascii(input_str):
    filtered_chars = input_str[24:89]
    distinct_chars = ''.join(set(filtered_chars))
    ascii_values = [ord(char) for char in distinct_values]
    ascii_values.sort()
    nth_ascii_value = ascii_values[10]
    for char in distinct_chars:
        if ord(char) == nth_ascii_value:
            return char