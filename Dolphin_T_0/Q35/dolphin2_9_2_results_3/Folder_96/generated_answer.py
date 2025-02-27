def remove_repeat_chars(string):
    char_count = {}
    for i in range(60, 200):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    repeating_chars = [char for char, count in char_count.items() if count > 1]
    for char in repeating_chars:
        string = string.replace(char, '')
    return string