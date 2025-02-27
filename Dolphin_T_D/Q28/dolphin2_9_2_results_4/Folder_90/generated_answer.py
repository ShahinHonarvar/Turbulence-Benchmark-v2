def return_nth_smallest_ascii(s):
    ascii_list = sorted([(s[i], ord(s[i])) for i in range(17, 84) if 17 <= i <= 83], key=lambda x: x[1])
    return ascii_list[4][0]