def filter_chars(s):
    l1 = [x for x in s if ord(x) >= ord('m') and ord(x) <= ord('w') and (25 <= ord(x) <= 97)]
    l2 = [x for x in s if x not in l1]
    return ''.join(l2)