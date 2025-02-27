def remove_repeat_chars(line):
    char_dict = {}
    for char in line[10:76]:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    for char, count in char_dict.items():
        if count > 1:
            line = line.replace(char, '')
    return line