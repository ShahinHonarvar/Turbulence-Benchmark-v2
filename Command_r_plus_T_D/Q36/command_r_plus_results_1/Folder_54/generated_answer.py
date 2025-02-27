def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[18:38] if ')' < char < 'P']
    result = []
    for char in s:
        if char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)