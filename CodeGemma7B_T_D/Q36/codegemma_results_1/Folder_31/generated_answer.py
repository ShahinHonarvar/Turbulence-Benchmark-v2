def filter_chars(str):
    alpha_lst = [chr(ord(i) + 5) for i in str if ord(i) in range(48, 102) and ord(i) not in range(66, 91) and (ord(i) not in range(97, 123))]
    return ''.join(alpha_lst)