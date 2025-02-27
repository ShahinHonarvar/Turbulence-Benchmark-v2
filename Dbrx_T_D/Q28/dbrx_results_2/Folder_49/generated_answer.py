def return_nth_smallest_ascii(char_string):
    ascii_values = {ord(char): char for i, char in enumerate(char_string) if 20 <= i <= 80}
    sorted_ascii_values = sorted(ascii_values.keys())
    return ascii_values.get(sorted_ascii_values[10], None)