def filter_chars(s):
    filter_list = [c for c in s if 45 < ord(c) < 57 and (not ord('F') < ord(c) < ord('n'))]
    return ''.join(filter_list)