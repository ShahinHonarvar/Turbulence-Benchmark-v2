def remove_repeat_chars(s):
    count_dict = {}
    for char in s[2:7]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    for char in count_dict:
        if count_dict[char] > 1:
            s = s.replace(char, '')
    return s