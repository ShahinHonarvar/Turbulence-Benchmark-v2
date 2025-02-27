def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[1:8] if 'L' <= c <= 'a']
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result