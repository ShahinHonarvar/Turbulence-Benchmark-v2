def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 7 or i > 9 or (ord(s[i]) < ord('6') or ord(s[i]) > ord('w')):
            result += s[i]
    return result