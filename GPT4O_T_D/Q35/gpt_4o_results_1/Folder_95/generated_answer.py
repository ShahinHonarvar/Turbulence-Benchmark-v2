def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    restricted_part = s[33:99]
    count_dict = {}
    for char in restricted_part:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    chars_to_remove = {char for char, count in count_dict.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 32 or s.index(char) >= 99))
    return result