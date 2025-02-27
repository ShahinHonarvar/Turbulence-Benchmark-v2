def return_nth_smallest_ascii(input_str):
    filtered_chars = input_str[5:11]
    ascii_values = sorted(set((ord(c) for c in filtered_chars)))
    return chr(ascii_values[5]) if len(ascii_values) >= 6 else None