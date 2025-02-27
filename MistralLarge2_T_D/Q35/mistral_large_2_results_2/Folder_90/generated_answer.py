def remove_repeat_chars(s):
    count_dict = {}
    for i, char in enumerate(s):
        if 306 < i < 807:
            count_dict[char] = count_dict.get(char, 0) + 1
    for char in count_dict:
        if count_dict[char] > 1:
            s = s.replace(char, '')
    return s