def remove_repeat_chars(string):
    count_dict = {}
    for i in range(1, 8):
        char = string[i]
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    result = ''
    for char in string:
        if count_dict.get(char, 0) > 1:
            continue
        result += char
    return result