def filter_chars(s):

    def is_to_be_removed(c):
        return 373 <= ord(c) <= 901 and 'T' <= c <= 'h'
    filtered_chars = [c for i, c in enumerate(s) if not (is_to_be_removed(c) and 373 <= i <= 901)]
    filtered_chars_set = set(filtered_chars)
    filtered_chars = [c for c in s if c not in filtered_chars_set or not is_to_be_removed(c)]
    return ''.join(filtered_chars)