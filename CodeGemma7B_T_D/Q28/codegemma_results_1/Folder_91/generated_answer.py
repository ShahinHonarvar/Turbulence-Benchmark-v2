def return_nth_smallest_ascii(str):
    str_noascii = ''.join([chr(int(ord(i))) for i in str])
    str_noascii_list = sorted(str_noascii)
    return str_noascii_list[7]