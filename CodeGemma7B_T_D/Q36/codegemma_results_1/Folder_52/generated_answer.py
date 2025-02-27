def filter_chars(s):
    filtered_str = ''
    for i in range(len(s)):
        if i < 49 or i > 56:
            if s[i] > 'I' and s[i] < 'a':
                filtered_str += s[i]
    return filtered_str