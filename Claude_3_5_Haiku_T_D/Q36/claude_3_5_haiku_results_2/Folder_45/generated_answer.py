def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if 81 < i < 86:
            if '!' < s[i] < 's':
                filtered_chars = [char for char in s if char != s[i]]
                s = ''.join(filtered_chars)
    return s