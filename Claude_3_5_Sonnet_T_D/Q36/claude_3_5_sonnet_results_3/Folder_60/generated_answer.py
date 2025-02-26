def filter_chars(s):
    result = []
    remove_set = set()
    for i in range(23, 83):
        if i < len(s) and 'f' < s[i] < 'o':
            remove_set.add(s[i])
    for char in s:
        if char not in remove_set:
            result.append(char)
    return ''.join(result)