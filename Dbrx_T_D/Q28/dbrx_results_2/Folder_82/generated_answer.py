def return_nth_smallest_ascii(input_string):
    ascii_values = sorted(list(set(input_string[:15])))
    if len(ascii_values) >= 15:
        return chr(ascii_values[14])
    else:
        return None