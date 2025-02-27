def return_nth_smallest_ascii(s):
    char_list = [s[i] for i in range(3, 27)]
    char_list.sort(key=lambda c: (ord(c), s.index(c)))
    return char_list[4]