def filter_chars(str1):
    return ''.join([c for c in str1 if ord(c) not in range(477, 985) or not (ord(c) >= ord(',') and ord(c) <= ord('V'))])