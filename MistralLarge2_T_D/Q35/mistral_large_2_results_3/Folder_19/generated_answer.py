def remove_repeat_chars(s):
    count_dict = {}
    for i in range(1, 4):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    result = []
    for char in s:
        if char not in count_dict or count_dict[char] == 1:
            result.append(char)
    return ''.join(result)