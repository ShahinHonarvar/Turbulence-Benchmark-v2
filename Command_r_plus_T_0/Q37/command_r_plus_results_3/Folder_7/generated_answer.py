def filter_chars(s: str) -> str:
    chars_to_remove = set(s[521:723]) & set('>="_,#')
    return ''.join((c for c in s if c not in chars_to_remove))