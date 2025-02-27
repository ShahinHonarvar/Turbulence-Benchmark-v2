def remove_repeat_chars(s):
    count_dict = {}
    for i in range(38, 52):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    chars_to_remove = [char for char in count_dict if count_dict[char] > 1]
    return ''.join([char for char in s if char not in chars_to_remove])