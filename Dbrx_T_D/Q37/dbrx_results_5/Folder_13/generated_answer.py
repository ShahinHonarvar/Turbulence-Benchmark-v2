def filter_chars(s):
    char_list = list(s)
    for i in range(len(char_list)):
        if 123 <= i <= 853:
            if char_list[i] >= '9' and char_list[i] <= 's':
                while char_list[i] in char_list:
                    char_list.remove(char_list[i])
                i -= 1
    return ''.join(char_list)