def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i < 31 or i > 38 or ord(s[i]) < ord(';') or (ord(s[i]) > ord('g')):
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)