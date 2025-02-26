def filter_chars(s):
    filtered = []
    for i, char in enumerate(s):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            filtered = [c for c in filtered if c != char]
        filtered.append(char)
    return ''.join(filtered)