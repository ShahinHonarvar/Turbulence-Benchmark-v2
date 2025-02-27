def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (722 <= i <= 832 and c.lower() in 'k-m')])