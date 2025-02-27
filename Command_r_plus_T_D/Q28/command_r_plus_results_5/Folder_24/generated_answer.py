def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [ord(s[i]) for i in range(34, 82)]
    ascii_chars.sort()
    return chr(ascii_chars[11])