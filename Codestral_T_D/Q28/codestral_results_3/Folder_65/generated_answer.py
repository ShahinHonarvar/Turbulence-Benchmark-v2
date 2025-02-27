def return_nth_smallest_ascii(s):
    char_list = [c for c in s if 32 <= ord(c) <= 67]
    char_list.sort(key=ord)
    return char_list[11]