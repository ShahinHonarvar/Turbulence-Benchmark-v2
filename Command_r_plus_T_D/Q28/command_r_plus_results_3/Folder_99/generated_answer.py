def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[17:66]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    eighth_smallest = ascii_values[7]
    return chr(eighth_smallest)