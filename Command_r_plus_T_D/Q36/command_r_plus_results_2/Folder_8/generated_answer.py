def filter_chars(s: str) -> str:
    chars_to_remove = set(s[82:94])
    chars_to_remove = {c for c in chars_to_remove if c > '!' and c < '*'}
    s_list = list(s)
    s_list = [c for c in s_list if c not in chars_to_remove]
    return ''.join(s_list)