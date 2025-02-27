def remove_repeat_chars(s):
    count_dict = {}
    for i in range(30, 200):
        char = s[i]
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    new_s = ''
    for char in s:
        if count_dict.get(char, 0) <= 1:
            new_s += char
        else:
            count_dict[char] = 0
    return new_s