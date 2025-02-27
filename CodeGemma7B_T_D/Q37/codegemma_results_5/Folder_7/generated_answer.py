def filter_chars(s):
    result = []
    for i in range(len(s)):
        if i >= 521 and i <= 722:
            if s[i] >= '>' and s[i] <= '_':
                continue
        result.append(s[i])
    return ''.join(result)