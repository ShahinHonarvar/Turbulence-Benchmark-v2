def return_nth_smallest_ascii(s):
    ascii_range = [ord(char) for char in s if 25 <= ord(char) <= 64]
    sorted_range = sorted(ascii_range)[:6]
    return chr(sorted_range[5])