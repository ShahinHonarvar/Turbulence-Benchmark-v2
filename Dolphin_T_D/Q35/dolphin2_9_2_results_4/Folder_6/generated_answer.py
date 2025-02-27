def remove_repeat_chars(s):
    count_dict = {}
    repeat_chars = []
    for i in range(20, 93):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    for char, count in count_dict.items():
        if count > 1:
            repeat_chars.append(char)
    for char in repeat_chars:
        s = s.replace(char, '')
    return s