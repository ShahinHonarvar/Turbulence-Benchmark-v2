def return_n_greatest_chars(s):
    ascii_list = [ord(c) for c in s]
    ascii_list.sort(reverse=True)
    n_greatest_chars = [chr(i) for i in ascii_list[:54]]
    return n_greatest_chars