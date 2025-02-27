def filter_chars(str):
    filtered = []
    for i, char in enumerate(str):
        if i >= 61 and i <= 70 and (char >= '0') and (char <= '@'):
            continue
        filtered.append(char)
    return ''.join(filtered)