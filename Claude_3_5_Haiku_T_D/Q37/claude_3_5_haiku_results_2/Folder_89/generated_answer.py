def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 11 <= i <= 32 and '!' <= char <= '@':
            filtered_chars = [c for c in filtered_chars if c != char]
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)