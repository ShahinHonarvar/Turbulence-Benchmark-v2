def remove_repeat_chars(s):
    count_dict = {}
    for char in s:
        if ord(char) > 62 and ord(char) < 96:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    new_s = ''
    for char in s:
        if ord(char) > 62 and ord(char) < 96 and (count_dict[char] == 1):
            new_s += char
        elif ord(char) <= 62 or ord(char) >= 96:
            new_s += char
    return new_s