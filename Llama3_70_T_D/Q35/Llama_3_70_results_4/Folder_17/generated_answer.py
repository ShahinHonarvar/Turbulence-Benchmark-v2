def remove_repeat_chars(s):
    count = {}
    for i in range(73, 84):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    result = ''
    for char in s:
        if count.get(char, 1) == 1:
            result += char
    return result