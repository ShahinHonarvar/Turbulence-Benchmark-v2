def remove_repeat_chars(string):
    chars_between_306_and_807 = string[306:807]
    char_count = {}
    for char in chars_between_306_and_807:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    for char in repeat_chars:
        string = string.replace(char, '')
    return string