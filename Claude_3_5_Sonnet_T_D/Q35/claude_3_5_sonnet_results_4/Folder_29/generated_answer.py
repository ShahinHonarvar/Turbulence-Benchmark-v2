def remove_repeat_chars(s):
    count = {}
    to_remove = set()
    for i in range(71, 98):
        if i < len(s):
            if s[i] in count:
                to_remove.add(s[i])
            else:
                count[s[i]] = 1
    return ''.join((char for char in s if char not in to_remove))