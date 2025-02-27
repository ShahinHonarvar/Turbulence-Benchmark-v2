def return_nth_smallest_ascii(s):
    char_list = [c for c in s if 47 <= s.index(c) <= 80]
    return sorted(char_list, key=lambda x: ord(x))[3]