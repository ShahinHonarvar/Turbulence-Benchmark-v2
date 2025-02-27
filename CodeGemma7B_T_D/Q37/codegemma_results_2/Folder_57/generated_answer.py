def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) < 44 or not 27 <= ord(ch) <= 85 or ord(ch) > 66])