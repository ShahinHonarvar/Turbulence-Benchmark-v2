def remove_repeat_chars(s):
    count_dict = {}
    for char in s[20:93]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    chars_to_remove = [char for char, count in count_dict.items() if count > 1]
    return ''.join([char for char in s if char not in chars_to_remove])