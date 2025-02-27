def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) not in range(163, 658) or (ch <= '(' or ch >= ']')])