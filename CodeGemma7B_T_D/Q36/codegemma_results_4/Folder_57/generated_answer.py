def filter_chars(txt):

    def replacement(value):
        return value if ord(value) < ord('A') or ord(value) >= ord('U') else ''
    return ''.join(map(replacement, txt))