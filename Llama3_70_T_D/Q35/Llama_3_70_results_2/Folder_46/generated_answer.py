def remove_repeat_chars(s):
    count = {}
    for i in range(10, 79):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    new_s = ''
    for char in s:
        if char not in count or count[char] == 1:
            new_s += char
    return new_s