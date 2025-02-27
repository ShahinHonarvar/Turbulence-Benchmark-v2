def filter_chars(s):
    filtered_chars = []
    for char in s:
        if 19 <= s.index(char) <= 22:
            if char >= ']' and char <= 't':
                continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)