def remove_repeat_chars(s):
    count_dict = {}
    for i in range(45, 48):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    chars_to_remove = [key for key, value in count_dict.items() if value > 1]
    return ''.join([char for char in s if char not in chars_to_remove])