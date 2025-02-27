def remove_repeat_chars(s):
    count = {}
    for i in range(81, 86):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    for char, occurrences in count.items():
        if occurrences > 1:
            s = s.replace(char, '')
    return s