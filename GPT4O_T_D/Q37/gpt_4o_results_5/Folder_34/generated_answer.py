def filter_chars(s):
    if len(s) <= 62:
        return s
    characters_to_remove = {ch for ch in s[54:63] if ')' <= ch <= '9'}
    return ''.join((ch for ch in s if ch not in characters_to_remove))