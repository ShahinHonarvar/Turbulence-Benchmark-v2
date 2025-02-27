def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(6):
        if count[ord(s[i])] == 1:
            s = s.replace(s[i], '')
        else:
            count[ord(s[i])] += 1
    return s