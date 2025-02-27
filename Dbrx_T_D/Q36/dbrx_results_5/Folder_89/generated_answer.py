def filter_chars(s: str) -> str:
    start, end = (57, 69)
    chars_to_remove = {chr(i) for i in range(ord('(') + 1, ord('W'))}
    return ''.join((c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_remove))