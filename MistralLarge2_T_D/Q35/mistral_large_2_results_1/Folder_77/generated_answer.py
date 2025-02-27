def remove_repeat_chars(s):
    count = {}
    for i in range(355, 988):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    for char in count:
        if count[char] > 1:
            s = s.replace(char, '')
    return s