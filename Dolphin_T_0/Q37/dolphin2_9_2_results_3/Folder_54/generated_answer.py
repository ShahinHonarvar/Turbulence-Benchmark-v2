def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if not (46 <= i <= 85 and '-' <= char <= 'X') or char))