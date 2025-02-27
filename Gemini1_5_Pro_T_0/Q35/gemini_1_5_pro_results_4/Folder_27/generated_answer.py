def remove_repeat_chars(s):
    substring = s[87:89]
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i] == substring[j]:
                s = s.replace(substring[i], '')
    return s