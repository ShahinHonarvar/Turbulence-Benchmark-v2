def filter_chars(s: str) -> str:
    char_set = set(s[73:75])
    filtered_chars = [c for i, c in enumerate(s) if i < 73 or i > 74 or c not in char_set]
    return ''.join(filtered_chars)