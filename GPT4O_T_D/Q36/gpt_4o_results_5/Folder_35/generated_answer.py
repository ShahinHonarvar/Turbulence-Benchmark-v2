def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i <= 163 or i >= 658 or s[i] <= '(' or (s[i] >= ']'):
            filtered_string += s[i]
    return filtered_string