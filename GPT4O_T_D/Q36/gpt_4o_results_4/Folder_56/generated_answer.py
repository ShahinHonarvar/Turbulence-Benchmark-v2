def filter_chars(s):

    def char_to_remove(c):
        return '/' < c < 'J'
    chars_to_remove = set(s[32:50])
    chars_to_remove = {c for c in chars_to_remove if char_to_remove(c)}
    return ''.join((c for c in s if c not in chars_to_remove))