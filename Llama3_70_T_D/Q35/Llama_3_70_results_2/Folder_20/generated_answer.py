def remove_repeat_chars(s):
    count_dict = {}
    for char in s:
        if 27 < ord(char) < 96:
            count_dict[char] = count_dict.get(char, 0) + 1
    result = ''
    for char in s:
        if not 27 < ord(char) < 96 or count_dict[char] == 1:
            result += char
    return result