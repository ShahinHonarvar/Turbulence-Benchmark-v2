def filter_chars(word):
    while '*' in word and ord(word[word.index('*')]) in range(219, 403) and (ord(word[word.index('*') + 2]) != ord('7')):
        word.replace(word[word.index('*'):word.index('*') + 3], '')
    return word