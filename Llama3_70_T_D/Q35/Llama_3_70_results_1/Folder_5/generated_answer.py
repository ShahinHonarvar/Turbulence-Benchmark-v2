def remove_repeat_chars(s):
    count = {}
    for i in range(2, 8):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    for char, freq in count.items():
        if freq > 1:
            s = s.replace(char, '')
    return s