def filter_chars(s: str) -> str:
    start_index, end_index = (309, 591)
    chars_to_remove = set()
    for char in s[end_index:start_index]:
        if 'S' < char < 'm':
            chars_to_remove.add(char)
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)