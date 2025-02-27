def remove_repeat_chars(s):
    counts = {}
    for i in range(70, 98):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    remove_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join([c for c in s if c not in remove_chars])
    return result