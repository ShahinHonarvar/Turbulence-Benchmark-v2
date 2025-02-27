def filter_chars(s):

    def is_to_be_removed(c):
        return 25 <= ord(c) <= 97 and 'm' <= c <= 'w'

    def remove_char(s, c):
        return s.replace(c, '')
    for c in set(s):
        if is_to_be_removed(c):
            s = remove_char(s, c)
    return s