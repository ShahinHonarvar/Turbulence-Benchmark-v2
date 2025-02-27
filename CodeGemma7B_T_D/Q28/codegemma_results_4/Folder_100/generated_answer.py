def return_nth_smallest_ascii(str_in):
    list_ascii = [ord(i) for i in str_in[5:48] if ord(i) >= ord('a') and ord(i) <= ord('z')]
    list_ascii.sort()
    return chr(list_ascii[12])