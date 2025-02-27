def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 323 < s.index(char) < 526 and ')' < char < 'O':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)