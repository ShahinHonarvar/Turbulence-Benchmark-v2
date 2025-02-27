def remove_repeat_chars(s):
    count_dict = {}
    for i in range(70, 98):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    new_string = ''
    for char in s:
        if char not in count_dict or count_dict[char] == 1:
            new_string += char
    return new_string