def remove_repeat_chars(s):
    count_dict = {}
    for i in range(68, 99):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    result = ''
    for char in s:
        if char not in count_dict or count_dict[char] == 1:
            result += char
    return result