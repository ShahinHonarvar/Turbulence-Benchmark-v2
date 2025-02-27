def filter_chars(s):

    def is_to_be_removed(c):
        return 'K' < c < 'a'

    def remove_char(s, c):
        return s.replace(c, '')
    chars_to_remove = [s[i] for i in range(18, 95) if is_to_be_removed(s[i])]
    for c in chars_to_remove:
        s = remove_char(s, c)
    return s