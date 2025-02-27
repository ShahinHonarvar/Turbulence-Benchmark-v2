def remove_repeat_chars(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for index in range(10, 100):
        if char_freq[string[index]] > 1:
            string = string[:index] + string[index + 1:]
    return string