def filter_chars(str1):
    return ''.join([i for i in str1 if ord(i) >= 65 and ord(i) <= 85 and (ord(i) - ord('A') >= 52) and (ord(i) - ord('A') <= 81)])