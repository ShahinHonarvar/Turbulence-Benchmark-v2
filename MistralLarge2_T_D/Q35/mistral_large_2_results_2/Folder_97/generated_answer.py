def remove_repeat_chars(s):
    count = {}
    for i in range(34, 70):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    for char, freq in count.items():
        if freq > 1:
            s = s.replace(char, '')
    return s