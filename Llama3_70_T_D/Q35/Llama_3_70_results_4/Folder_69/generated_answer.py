def remove_repeat_chars(s):
    count_dict = {}
    for i in range(39, 43):
        if i < len(s):
            if s[i] in count_dict:
                count_dict[s[i]] += 1
            else:
                count_dict[s[i]] = 1
    to_remove = set()
    for char, count in count_dict.items():
        if count > 1:
            to_remove.add(char)
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result