def remove_repeat_chars(string):
    freq = {}
    for i in range(36, 86):
        if string[i] in freq:
            freq[string[i]] += 1
        else:
            freq[string[i]] = 1
    chars_to_remove = [char for char, count in freq.items() if count > 1]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string