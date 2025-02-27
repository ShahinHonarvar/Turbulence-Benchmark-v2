def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('+'), ord('8') + 1))
    result = []
    inside_range = False
    for i, c in enumerate(s):
        if i == 21:
            inside_range = True
        elif i == 43:
            inside_range = False
        if not inside_range or ord(c) not in chars_to_remove:
            result.append(c)
    return ''.join(result)