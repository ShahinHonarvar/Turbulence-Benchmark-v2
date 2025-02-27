def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = [ord(char) for char in s if 4 <= s.index(char) <= 33]
    if len(ascii_values) >= 4:
        return chr(sorted(ascii_values)[3])
    else:
        return ''