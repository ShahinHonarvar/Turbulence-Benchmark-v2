def return_nth_smallest_ascii(s):
    char_list = [c for c in s if 47 <= ord(c) <= 80]
    char_list.sort(key=ord)
    return char_list[3]