def remove_repeat_chars(s):
    count = {}
    for i in range(20, 43):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    to_remove = {char for char, occurrence in count.items() if occurrence > 1}
    return ''.join((char for char in s if char not in to_remove))