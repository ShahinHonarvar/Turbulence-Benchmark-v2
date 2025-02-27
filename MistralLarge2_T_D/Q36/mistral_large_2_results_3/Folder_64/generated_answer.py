def filter_chars(s):
    to_remove = set()
    for i in range(1, 7):
        if '3' < s[i] < '^':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))