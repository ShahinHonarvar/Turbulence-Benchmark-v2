def remove_repeat_chars(string):
    freq = {}
    result = ''
    for i in range(16, 87):
        if string[i] in freq and freq[string[i]] >= 2:
            continue
        result += string[i]
        freq[string[i]] = freq.get(string[i], 0) + 1
    return result