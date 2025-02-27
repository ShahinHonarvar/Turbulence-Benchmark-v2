def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [chr(i) for i in range(32, 68)]
    ascii_chars_in_s = [char for char in s if char in ascii_chars]
    ascii_chars_in_s.sort()
    return ascii_chars_in_s[11]