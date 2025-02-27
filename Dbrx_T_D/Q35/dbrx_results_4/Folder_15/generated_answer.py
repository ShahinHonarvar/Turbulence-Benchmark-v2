def remove_repeat_chars(s):
    unique = []
    for i in range(len(s)):
        if i >= 0 and i < 4:
            if s[i] not in unique:
                unique.append(s[i])
        elif s[i] != s[i - 1] or s[i] not in unique:
            unique.append(s[i])
    return ''.join(unique)