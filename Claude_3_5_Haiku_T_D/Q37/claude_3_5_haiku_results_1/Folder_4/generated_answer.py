def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 19 <= i <= 33 and 'S' <= char <= '{':
            filtered_chars = [c for c in filtered_chars if c != char]
        filtered_chars.append(char)
    return ''.join(filtered_chars)