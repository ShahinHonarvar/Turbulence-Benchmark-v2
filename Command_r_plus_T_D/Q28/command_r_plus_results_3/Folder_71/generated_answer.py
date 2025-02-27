def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[5:83]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    nth_smallest = ascii_values[15]
    return chr(nth_smallest)