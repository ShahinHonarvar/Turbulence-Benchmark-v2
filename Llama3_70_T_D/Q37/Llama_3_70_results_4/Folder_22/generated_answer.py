def filter_chars(s):

    def is_to_remove(c):
        return 33 <= ord(c) <= 70 and '7' <= c <= 'k'
    chars_to_remove = {c for c in set(s) if is_to_remove(c)}
    return ''.join((c for c in s if c not in chars_to_remove))