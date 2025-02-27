def filter_chars(s):
    for c in range(ord('J'), ord('b') + 1):
        for i in range(348, 853):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s