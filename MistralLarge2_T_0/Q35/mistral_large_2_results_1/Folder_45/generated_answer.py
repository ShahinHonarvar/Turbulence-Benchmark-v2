def remove_repeat_chars(s):
    count = {}
    for i in range(40, 200):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))