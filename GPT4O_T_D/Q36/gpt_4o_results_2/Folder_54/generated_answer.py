def filter_chars(s):

    def char_to_remove(c):
        return ')' < c < 'P'
    chars_to_remove = {c for c in s[19:38] if char_to_remove(c)}
    return ''.join((c for c in s if c not in chars_to_remove))