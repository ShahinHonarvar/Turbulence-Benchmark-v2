def filter_chars(s: str) -> str:
    chars_to_remove = set(s[299:418])
    chars_to_remove = {char for char in chars_to_remove if '9' < char < 'P'}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)