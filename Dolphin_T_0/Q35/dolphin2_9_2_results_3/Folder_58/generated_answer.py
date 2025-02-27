def remove_repeat_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    multiple_chars = [char for char, count in char_count.items() if count > 1]
    new_string = ''
    for char in string:
        if char not in multiple_chars:
            new_string += char
    return new_string