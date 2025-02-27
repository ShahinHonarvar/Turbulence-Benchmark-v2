def filter_chars(s):
    if len(s) > 92:
        subsequence = s[42:93]
        chars_to_remove = {ch for ch in subsequence if '/' <= ch <= 'a'}
        return ''.join((ch for ch in s if ch not in chars_to_remove))
    return s