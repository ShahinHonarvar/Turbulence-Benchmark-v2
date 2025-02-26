def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 21 <= i <= 43 and '+' <= char <= '8':
            filtered_chars.extend((c for c in s if c != char))
            break
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)