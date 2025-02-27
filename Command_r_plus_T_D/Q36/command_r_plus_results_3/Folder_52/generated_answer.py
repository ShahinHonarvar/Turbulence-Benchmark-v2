def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(49, 57) if chr(i) > 'I' and chr(i) < 'a']
    return ''.join((c for c in s if c not in chars_to_remove))