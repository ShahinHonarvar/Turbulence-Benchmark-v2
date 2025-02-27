def remove_repeat_chars(s):
    count_dict = {}
    for i in range(86, 89):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    to_remove = [char for char, count in count_dict.items() if count > 1]
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result