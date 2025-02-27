def filter_chars(s: str) -> str:
    start, end = (4, 8)
    chars_to_remove = {chr(i): None for i in range(ord('1') + 1, ord('J'))}

    def filter_char(c):
        if start <= i < end and c in chars_to_remove:
            return ''
        return c
    return ''.join((filter_char(c) for i, c in enumerate(s)))