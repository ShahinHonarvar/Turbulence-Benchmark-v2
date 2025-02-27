def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 12 and i <= 25 and (ord(s[i]) >= ord('P')) and (ord(s[i]) <= ord('x')):
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result