def filter_chars(s):
    to_remove = set()
    for i in range(299, 418):
        if '9' < s[i] < 'P':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))