def filter_chars(s):
    for char in range(ord('W'), ord('{')):
        for i in range(15, 56):
            if s[i] == chr(char):
                s = s.replace(chr(char), '')
    return s