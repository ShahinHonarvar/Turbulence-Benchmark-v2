def return_nth_smallest_ascii(s):
    char_list = [s[i] for i in range(25, 89)]
    char_list = sorted(set(char_list), key=lambda x: ord(x))
    if len(char_list) < 11:
        return None
    return char_list[10]