def remove_repeat_chars(s):
    count_dict = {}
    for char in s[13:91]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    result = ''
    for char in s:
        if count_dict.get(char, 0) <= 1:
            result += char
    return result