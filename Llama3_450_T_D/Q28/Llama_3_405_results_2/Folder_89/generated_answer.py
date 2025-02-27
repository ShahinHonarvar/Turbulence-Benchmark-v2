def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[24:72])
    ascii_values = [ord(c) for c in sorted_chars]
    eighth_smallest = sorted(ascii_values)[7]
    return chr(eighth_smallest)