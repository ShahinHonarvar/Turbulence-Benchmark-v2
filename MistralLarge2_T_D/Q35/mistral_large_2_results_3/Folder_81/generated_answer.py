def remove_repeat_chars(s):
    count = {}
    for i in range(20, 200):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    for char in count:
        if count[char] > 1:
            s = s.replace(char, '')
    return s