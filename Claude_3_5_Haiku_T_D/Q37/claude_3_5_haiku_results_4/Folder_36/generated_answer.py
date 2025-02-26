def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 259 <= i <= 502 and ',' <= char <= '3':
            filtered_chars.extend((c for c in s if c != char))
            break
        filtered_chars.append(char)
    return ''.join(filtered_chars) if filtered_chars else s