def remove_repeat_chars(s):
    count_dict = {}
    for i in range(90, 200):
        if i < len(s):
            char = s[i]
            count_dict[char] = count_dict.get(char, 0) + 1
    return ''.join([char for char in s if count_dict.get(char, 0) == 1 or count_dict.get(char, 1) == 0])