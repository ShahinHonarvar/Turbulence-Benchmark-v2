def remove_repeat_chars(s):
    for i in range(29, 53):
        for j in range(i + 1, 53):
            if s[i] == s[j]:
                s = list(s)
                for k in range(len(s)):
                    if s[k] == s[i]:
                        s.pop(k)
                s = ''.join(s)
    return s