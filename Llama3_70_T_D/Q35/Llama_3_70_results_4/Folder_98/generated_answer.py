def remove_repeat_chars(s):
    count_dict = {}
    for char in s[:8]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    result = ''
    for char in s:
        if char not in count_dict or count_dict[char] == 1:
            result += char
    return result