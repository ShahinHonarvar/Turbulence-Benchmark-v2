def remove_repeat_chars(string):
    char_count = {}
    start_index = 44
    end_index = 67
    for i in range(len(string)):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for char in char_count:
        if char_count[char] > 1 and start_index <= i < end_index:
            string = string.replace(char, '', char_count[char] - 1)
    return string