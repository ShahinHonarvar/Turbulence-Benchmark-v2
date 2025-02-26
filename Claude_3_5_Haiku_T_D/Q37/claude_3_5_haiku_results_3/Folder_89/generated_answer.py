def filter_chars(s):
    to_remove = set()
    for i in range(11, 33):
        if i < len(s) and '!' <= s[i] <= '@':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))