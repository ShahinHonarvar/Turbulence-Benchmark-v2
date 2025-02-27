def return_n_greatest_chars(string_arg):
    ascii_list = sorted([ord(c) for c in string_arg], reverse=True)
    result = [chr(i) for i in ascii_list[:37]]
    return result