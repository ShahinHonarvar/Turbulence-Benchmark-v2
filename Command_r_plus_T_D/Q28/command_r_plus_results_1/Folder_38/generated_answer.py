def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [char for char in s[:46] if 32 <= ord(char) <= 126]
    ascii_chars.sort(key=lambda x: ord(x))
    return ascii_chars[9] if len(ascii_chars) > 9 else ''