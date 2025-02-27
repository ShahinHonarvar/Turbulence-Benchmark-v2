def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for char in s[318:338]:
        if 'B' < char < 'z':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))