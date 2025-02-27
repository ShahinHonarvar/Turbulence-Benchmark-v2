def return_nth_smallest_ascii(s):
    char_list = [ch for ch in s[22:75]]
    char_list.sort(key=lambda x: ord(x))
    return char_list[11]