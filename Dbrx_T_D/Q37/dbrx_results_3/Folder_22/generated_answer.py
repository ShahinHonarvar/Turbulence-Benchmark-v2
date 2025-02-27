def filter_chars(s):
    char_list = [c for c in s if ord('7') <= ord(c) <= ord('k') or (ord(c) < 33 or ord(c) > 70)]
    return ''.join(char_list)