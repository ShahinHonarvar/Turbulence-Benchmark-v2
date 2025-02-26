def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 28 <= i <= 65 and 'O' <= char <= 'd':
            filtered_chars = [c for c in filtered_chars if c != char]
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)