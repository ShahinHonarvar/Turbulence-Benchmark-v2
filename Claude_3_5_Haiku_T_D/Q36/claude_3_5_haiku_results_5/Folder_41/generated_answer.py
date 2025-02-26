def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if 81 < i < 89 and 'f' < char < '{':
            filtered_chars = [c for c in filtered_chars if c != char]
        filtered_chars.append(char)
    return ''.join(filtered_chars)