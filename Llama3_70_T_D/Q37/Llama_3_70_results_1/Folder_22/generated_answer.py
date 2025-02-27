def filter_chars(s):

    def char_filter(c):
        return ord(c) < 33 or ord(c) > 70 or c < '7' or (c > 'k')
    result = ''
    for c in s:
        if char_filter(c):
            result += c
    return result