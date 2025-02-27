def remove_repeat_chars(s):
    counts = {}
    for i in range(80, 200):
        if i < len(s):
            counts[s[i]] = counts.get(s[i], 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))