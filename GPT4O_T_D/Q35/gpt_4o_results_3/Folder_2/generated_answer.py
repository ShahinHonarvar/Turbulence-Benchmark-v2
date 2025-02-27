def remove_repeat_chars(s):
    if len(s) <= 1:
        return s
    middle_segment = s[73:93]
    count_dict = {}
    for char in middle_segment:
        count_dict[char] = count_dict.get(char, 0) + 1
    repeat_chars = {char for char, count in count_dict.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)