def filter_chars(word):
    return ''.join([a for a in word if ord(a) <= ord('T') and a == word[i] and (20 <= i <= 79)])