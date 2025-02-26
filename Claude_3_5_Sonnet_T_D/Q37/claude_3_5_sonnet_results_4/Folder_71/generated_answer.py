def filter_chars(s):
    result = ''
    remove_set = set()
    for i in range(32, 47):
        if i < len(s) and '0' <= s[i] <= 'k':
            remove_set.add(s[i])
    for char in s:
        if char not in remove_set:
            result += char
    return result