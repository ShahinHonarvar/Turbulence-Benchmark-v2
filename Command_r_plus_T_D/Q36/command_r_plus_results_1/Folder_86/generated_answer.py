def filter_chars(s: str) -> str:
    chars_to_remove = set(s[672:710])
    chars_to_remove = {c for c in chars_to_remove if 'X' < c < '}'}
    s_filtered = ''.join((c for c in s if c not in chars_to_remove))
    return s_filtered