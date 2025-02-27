def remove_repeat_chars(s):
    counts = {}
    for i in range(68, 99):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    removed_chars = set([char for char, count in counts.items() if count > 1])
    result = ''.join([char for char in s if char not in removed_chars])
    return result