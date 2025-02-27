def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if i in range(19, 91) and 'F' <= s[i] <= 'h':
            if s[i] not in filtered_chars:
                filtered_chars.append(s[i])
    result = []
    for i in range(len(s)):
        if s[i] not in filtered_chars:
            result.append(s[i])
    return ''.join(result)