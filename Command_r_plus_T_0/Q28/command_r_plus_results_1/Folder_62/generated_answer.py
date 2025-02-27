def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[51:79]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    ninth_smallest = ascii_values[8]
    return chr(ninth_smallest)