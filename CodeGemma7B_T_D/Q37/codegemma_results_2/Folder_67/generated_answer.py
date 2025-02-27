def filter_chars(text):
    filtered = []
    for i, char in enumerate(text):
        if 19 <= i <= 22 and char > ']' and (char <= 't'):
            continue
        filtered.append(char)
    return ''.join(filtered)