def return_nth_smallest_ascii(s):
    ascii_list = []
    for i in range(50, 76):
        if s[i].isalpha() or s[i].isdigit() or s[i].isalnum():
            ascii_list.append(ord(s[i]))
    ascii_list.sort()
    return chr(ascii_list[6])