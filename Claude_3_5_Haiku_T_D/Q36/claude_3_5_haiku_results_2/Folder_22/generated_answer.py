def filter_chars(s):
    chars_to_remove = set(s[56:84] if 56 < len(s) and 84 < len(s) else [])
    filtered_chars = [c for c in chars_to_remove if ';' < c < 'z']
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)