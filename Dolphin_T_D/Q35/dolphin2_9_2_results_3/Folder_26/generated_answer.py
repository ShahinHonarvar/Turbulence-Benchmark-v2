def remove_repeat_chars(s):
    count = [0] * 128
    for i in range(68, 99):
        if count[ord(s[i])] == 1:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            count[ord(s[i])] += 1
    return s