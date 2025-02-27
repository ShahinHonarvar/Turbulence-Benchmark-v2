def return_nth_smallest_ascii(input_string):
    relevant_chars = input_string[51:61]
    ascii_values = [ord(char) for char in relevant_chars]
    if len(ascii_values) >= 5:
        fifth_smallest_ascii = sorted(ascii_values)[:5][-1]
    else:
        return None
    return chr(fifth_smallest_ascii)