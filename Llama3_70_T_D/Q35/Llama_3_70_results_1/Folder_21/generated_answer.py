def remove_repeat_chars(s):
    count_dict = {}
    for char in s[462:995]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeat_chars = [key for key, value in count_dict.items() if value > 1]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result