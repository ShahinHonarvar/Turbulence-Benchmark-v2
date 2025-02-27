def remove_repeat_chars(s):
    count_dict = {}
    for i in range(70, 200):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    new_string = ''
    for char in s:
        if count_dict.get(char, 0) <= 1:
            new_string += char
    return new_string