def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [char for char in s[18:67]]
    ascii_chars.sort(key=ord)
    return ascii_chars[18]