def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(37, 43):
        count[ord(s[i])] += 1
    for i in range(256):
        if count[i] > 1:
            s = s.replace(chr(i), '')
    return s