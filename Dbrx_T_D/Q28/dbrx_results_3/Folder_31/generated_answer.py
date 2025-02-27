def return_nth_smallest_ascii(ascii_string):
    ascii_values = [ord(char) for char in ascii_string if ord(char) >= 10 and ord(char) <= 82]
    sorted_ascii_values = sorted(ascii_values)[17]
    return chr(sorted_ascii_values)