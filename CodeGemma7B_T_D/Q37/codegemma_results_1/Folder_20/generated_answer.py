def filter_chars(text):
    filtered = []
    for i, char in enumerate(text):
        if i >= 25 and i <= 97 and (char >= 'm') and (char <= 'w'):
            continue
        filtered.append(char)
    return ''.join(filtered)