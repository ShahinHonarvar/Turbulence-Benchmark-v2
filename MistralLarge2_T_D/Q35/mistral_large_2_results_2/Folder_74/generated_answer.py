def remove_repeat_chars(s):
    count = {}
    for i in range(69, 97):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    for char, cnt in count.items():
        if cnt > 1:
            s = s.replace(char, '')
    return s