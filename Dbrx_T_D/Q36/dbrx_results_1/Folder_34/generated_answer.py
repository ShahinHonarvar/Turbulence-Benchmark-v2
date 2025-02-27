def filter_chars(s):
    for i in range(len(s)):
        if ord('?') < ord(s[i]) < ord('m') and 10 <= i <= 78:
            s = s[:i] + s[i + 1:]
            i -= 1
    return s