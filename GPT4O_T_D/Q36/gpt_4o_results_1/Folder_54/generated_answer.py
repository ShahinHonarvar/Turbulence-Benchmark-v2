def filter_chars(s):

    def should_filter(c):
        return ')' < c < 'P'
    filtered_chars = {c for i, c in enumerate(s) if 18 < i < 38 and should_filter(c)}
    return ''.join((c for c in s if c not in filtered_chars))