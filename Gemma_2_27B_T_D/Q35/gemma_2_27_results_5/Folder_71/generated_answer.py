def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 35):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    remove = [char for char, count in counts.items() if count > 1]
    result = []
    for char in s:
        if char not in remove:
            result.append(char)
    return ''.join(result)