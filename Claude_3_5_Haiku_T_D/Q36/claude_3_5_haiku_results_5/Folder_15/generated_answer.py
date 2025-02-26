def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if 2 < i < 7 and 'h' < s[i] < 'k':
            filtered_chars = [char for char in filtered_chars if char != s[i]]
        else:
            filtered_chars.append(s[i])
    return ''.join(filtered_chars)