def filter_chars(text):
    return ''.join((c for i, c in enumerate(text) if i not in range(43, 69) or ord(c) <= ord('B') or ord(c) >= ord('r')))