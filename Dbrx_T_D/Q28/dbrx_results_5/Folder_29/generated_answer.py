def return_nth_smallest_ascii(s: str) -> str:
    chars = sorted(s)[5:11]
    if len(chars) < 6:
        raise ValueError('Less than 6 characters between indices 5 to 10')
    return chars[5]