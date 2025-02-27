def remove_repeat_chars(s):
    s_list = list(s)
    char_count = {}
    for i in range(101, 200):
        if i < len(s_list):
            char = s_list[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s_list if char not in chars_to_remove]
    return ''.join(result)