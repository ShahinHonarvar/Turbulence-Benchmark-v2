def return_nth_smallest_ascii(s):
    char_list = [c for c in s if 48 <= ord(c) <= 76]
    char_list.sort(key=lambda c: ord(c))
    if len(char_list) < 5:
        return None
    else:
        return char_list[4]