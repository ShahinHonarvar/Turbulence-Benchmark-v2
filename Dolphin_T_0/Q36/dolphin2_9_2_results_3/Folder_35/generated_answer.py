def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 163 <= i < 658 and (char > '(' and char < ']'):
            result.append(''.join((s[j] for j in range(len(s)) if s[j] != char)))
    return ''.join(result)