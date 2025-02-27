def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 70):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join([char for char in s if char not in to_remove])
    return result