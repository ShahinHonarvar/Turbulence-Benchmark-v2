def filter_chars(s):

    def is_to_remove(char):
        return 32 <= ord(char) <= 46 and '0' <= char <= 'k'

    def remove_chars(s, char):
        return s.replace(char, '')
    for char in s:
        if is_to_remove(char):
            s = remove_chars(s, char)
    return s