def remove_repeat_chars(string):
    freq = {}
    for i in range(6):
        if string[i] in freq:
            freq[string[i]] += 1
        else:
            freq[string[i]] = 1
    for char, count in freq.items():
        if count > 1:
            string = string.replace(char, '')
    return string