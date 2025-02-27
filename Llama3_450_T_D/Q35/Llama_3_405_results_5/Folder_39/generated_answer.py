def remove_repeat_chars(s):
    count_dict = {}
    for char in s[44:91]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeat_chars = [char for char, count in count_dict.items() if count > 1]
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s