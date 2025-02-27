def remove_repeat_chars(string):
    counts = {}
    for i in range(10, 28):
        if string[i] in counts:
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
    chars_to_remove = [char for char, count in counts.items() if count > 1]
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string