def remove_repeat_chars(string):
    freq = {}
    for i in range(30, 200):
        if string[i] in freq:
            freq[string[i]] += 1
        else:
            freq[string[i]] = 1
    to_remove = [k for k, v in freq.items() if v > 1]
    new_string = ''
    for i in range(len(string)):
        if string[i] not in to_remove:
            new_string += string[i]
    return new_string