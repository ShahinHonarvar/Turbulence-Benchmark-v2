def filter_chars(s):
    return ''.join([c for c in s if not 10 <= idx <= 52 or not '@' <= c <= 'T' for idx, c in enumerate(s)])