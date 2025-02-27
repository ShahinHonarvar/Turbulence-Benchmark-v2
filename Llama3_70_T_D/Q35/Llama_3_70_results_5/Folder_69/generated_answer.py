def remove_repeat_chars(s):
    count = {}
    for i in range(39, 43):
        count[s[i]] = count.get(s[i], 0) + 1
    to_remove = set()
    for char, freq in count.items():
        if freq > 1:
            to_remove.add(char)
    return ''.join([c for c in s if c not in to_remove])