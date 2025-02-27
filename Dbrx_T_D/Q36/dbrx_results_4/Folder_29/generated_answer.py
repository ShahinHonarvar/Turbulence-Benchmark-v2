def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(46, 68):
        if char_list[i] > 'H' and char_list[i] < 's':
            char_list = [c for c in char_list if c != char_list[i]]
    return ''.join(char_list)