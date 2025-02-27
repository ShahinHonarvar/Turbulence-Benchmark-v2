def remove_repeat_chars(input_str):
    char_count = {}
    for char in input_str:
        if 48 <= ord(char) <= 76 and char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            input_str = input_str.replace(char, '')
    return input_str