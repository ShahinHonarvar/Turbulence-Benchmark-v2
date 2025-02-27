def remove_repeat_chars(s):
    chars = {}
    for i in range(36, 54):
        if s[i] in chars and chars[s[i]]:
            s = s[:i] + s[i + 1:]
            for j in range(i, len(s)):
                if s[j] == s[j - 1]:
                    s = s[:j] + s[j + 1:]
    return s