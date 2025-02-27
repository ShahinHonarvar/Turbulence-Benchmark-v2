def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[3:9] if '*' < char < 'E']
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)