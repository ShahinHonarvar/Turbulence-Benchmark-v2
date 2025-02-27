def filter_chars(arg_1):
    final_str = ''.join([char for char in arg_1 if char not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm' and (ord(char) < 603 or ord(char) > 759)])
    return final_str