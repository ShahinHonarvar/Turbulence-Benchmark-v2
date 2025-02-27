def remove_repeat_chars(string):
    char_count = {}
    for char in string:
        if char.isalpha() or char.isdigit():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    new_string = ''
    for char in string:
        if char.isalpha() or char.isdigit():
            if char_count[char] == 1:
                new_string += char
    return new_string