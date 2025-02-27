def remove_repeat_chars(s):
    for i in range(70, 98):
        chars = [s[j] for j in range(i + 1, 98) if s[j] == s[i]]
        if len(chars) > 0:
            s = ''.join([c for c in s if c not in set(chars)])
    return s