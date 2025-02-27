def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if i > 73 and i < 84:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s