def filter_chars(s):
    for char in range(ord('0'), ord('9') + 1):
        for i in range(299, 418):
            if s[i] == chr(char):
                s = s.replace(chr(char), '')
    return s