def remove_repeat_chars(s):
    count = {}
    for i in range(6, 9):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in count:
        if count[char] > 1:
            s = s.replace(char, '')
    return s