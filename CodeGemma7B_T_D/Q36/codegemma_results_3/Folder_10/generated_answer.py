def filter_chars(word):
    word = word[:35] + ''.join([i for i in word[35:60] if i not in word[35:60] or ord(i) > ord('!') or ord(i) < ord('B')]) + word[60:]
    return word