def remove_repeat_chars(s):
    count = {}
    result = list(s)
    for i in range(19, 60):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    for char, occurrences in count.items():
        if occurrences > 1:
            result = [c for c in result if c != char]
    return ''.join(result)