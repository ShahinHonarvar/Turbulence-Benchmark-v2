def filter_chars(word):
    return ''.join([w for w in word if w < 'O' or w > '^' or (not (ord(w) >= 17 and ord(w) <= 63))])