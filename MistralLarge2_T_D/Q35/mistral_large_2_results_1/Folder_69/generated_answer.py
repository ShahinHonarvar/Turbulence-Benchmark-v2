def remove_repeat_chars(s):
    count = {}
    for i in range(39, 43):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] in count and count[s[i]] > 1:
            s = s[:i] + s[i + 1:]
    return s