def filter_chars(text):
    a = ''.join(list(filter(lambda x: not (text.index(x) in range(11, 72) and x >= 'i' and (x <= 'v')), text)))
    return a