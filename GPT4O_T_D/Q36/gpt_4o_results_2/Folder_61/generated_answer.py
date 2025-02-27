def filter_chars(s):

    def should_remove(c):
        return '*' < c < 'E'
    indices_to_check = range(4, 9)
    chars_to_remove = {s[i] for i in indices_to_check if i < len(s) and should_remove(s[i])}
    return ''.join((c for c in s if c not in chars_to_remove))