def remove_repeat_chars(s):
    count_dict = {}
    for char in s[36:52]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeat_chars = set([char for char in count_dict if count_dict[char] > 1])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result