def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 21 <= i <= 43 and '+' <= s[i] <= '8':
            filtered_chars += s[i]
    result = ''
    for c in s:
        if c not in filtered_chars:
            result += c
    return result