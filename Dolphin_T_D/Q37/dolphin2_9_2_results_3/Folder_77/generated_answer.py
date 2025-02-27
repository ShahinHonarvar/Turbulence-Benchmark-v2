def filter_chars(s):
    return ''.join((ch for i, ch in enumerate(s) if i < 384 or i > 411 or (ch < '/' or ch > '8') or (i >= 384 and i <= 411 and (ch >= '/' and ch <= '8'))))