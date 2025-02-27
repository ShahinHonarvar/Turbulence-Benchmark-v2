def filter_chars(word):
    return ''.join([char for char in word if not (227 <= ord(char) <= 235 and 'D' <= char <= 'u')])