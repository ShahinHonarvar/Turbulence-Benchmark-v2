def filter_chars(s):
    for char in range(348, 853):
        if s[char] >= 'J' and s[char] <= 'b':
            s = s[:char] + s[char + 1:]
    return s