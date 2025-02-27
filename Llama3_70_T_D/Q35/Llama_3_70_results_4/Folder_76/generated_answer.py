def remove_repeat_chars(s):
    count = {}
    for i in range(330, 543):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    new_s = ''
    for char in s:
        if count.get(char, 0) < 2:
            new_s += char
    return new_s