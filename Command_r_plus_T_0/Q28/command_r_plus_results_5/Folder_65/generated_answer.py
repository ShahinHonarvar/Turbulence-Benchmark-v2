def return_nth_smallest_ascii(s: str) -> str:
    ascii_range = [chr(i) for i in range(32, 68)]
    char_set = set(s)
    common_chars = list(char_set.intersection(ascii_range))
    common_chars.sort(key=ord)
    return common_chars[11] if len(common_chars) > 11 else ''