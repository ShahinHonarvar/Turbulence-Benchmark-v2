def filter_chars(s):
    filtered_chars = list(s)
    for i in range(1, min(6, len(s))):
        if '$' <= s[i] <= ';':
            filtered_chars = [char for char in filtered_chars if char != s[i]]
    return ''.join(filtered_chars)