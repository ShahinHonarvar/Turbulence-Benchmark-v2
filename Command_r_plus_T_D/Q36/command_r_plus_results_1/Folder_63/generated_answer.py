def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 26 <= s.index(char) < 80 and char > '<' and (char < '>'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)