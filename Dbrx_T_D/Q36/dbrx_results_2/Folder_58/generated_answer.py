def filter_chars(s: str) -> str:
    start_index = 318
    end_index = 337
    chars_to_remove = set(range(ord('B') + 1, ord('z'))) - set(range(ord(s[start_index]), ord(s[end_index - 1]) + 1))
    result = ''.join((c for i, c in enumerate(s) if i < start_index or i >= end_index or ord(c) not in chars_to_remove))
    return result