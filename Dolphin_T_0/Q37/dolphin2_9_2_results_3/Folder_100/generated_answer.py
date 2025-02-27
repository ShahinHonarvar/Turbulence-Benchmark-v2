def filter_chars(s):
    filtered_string = [c for c in s if ord(c) >= ord('J') and ord(c) <= ord('Q') and (88 <= s.index(c) <= 90)]
    return ''.join(filtered_string)