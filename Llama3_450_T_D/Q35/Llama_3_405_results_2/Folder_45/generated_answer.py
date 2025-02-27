def remove_repeat_chars(input_str):
    char_count = {}
    for i in range(40, 200):
        if i < len(input_str):
            char = input_str[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    chars_to_remove = set([char for char, count in char_count.items() if count > 1])
    result_str = ''
    for char in input_str:
        if char not in chars_to_remove:
            result_str += char
    return result_str