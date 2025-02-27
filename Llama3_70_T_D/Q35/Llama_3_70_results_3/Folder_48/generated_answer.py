def remove_repeat_chars(s):
    char_count = {}
    for i in range(409, 502):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    new_s = []
    for char in s:
        if char not in char_count or char_count[char] == 1:
            new_s.append(char)
    return ''.join(new_s)