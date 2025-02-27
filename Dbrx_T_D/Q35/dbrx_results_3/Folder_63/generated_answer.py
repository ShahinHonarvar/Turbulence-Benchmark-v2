def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for i in range(81, 87):
        if s[i] in char_count and char_count[s[i]] > 1:
            s = s[:i] + s[i + 1:]
            i -= 1
    return s