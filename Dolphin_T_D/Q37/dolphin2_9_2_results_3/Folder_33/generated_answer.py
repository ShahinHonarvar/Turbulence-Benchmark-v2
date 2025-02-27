def filter_chars(s):
    return ''.join([c for c in s if (ord(c) < ord('K') or ord(c) > ord('m')) or (ord('K') <= ord(c) <= ord('m') and (ord('m') <= ord('K') or 722 <= s.index(c) <= 832))])