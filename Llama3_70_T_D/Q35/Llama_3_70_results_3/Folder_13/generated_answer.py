def remove_repeat_chars(s):
    count_dict = {}
    for char in s[46:91]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeat_chars = set()
    for char, count in count_dict.items():
        if count > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result