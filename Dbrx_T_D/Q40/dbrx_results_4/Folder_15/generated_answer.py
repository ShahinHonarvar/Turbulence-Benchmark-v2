def return_n_smallest_chars(s):
    ascii_list = [ord(c) for c in s]
    ascii_list.sort()
    return [chr(i) for i in ascii_list[:57]]