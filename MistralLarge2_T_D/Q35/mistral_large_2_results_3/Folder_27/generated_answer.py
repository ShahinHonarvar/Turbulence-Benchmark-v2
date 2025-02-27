def remove_repeat_chars(s):
    counts = {}
    for i in range(86, 89):
        if i < len(s):
            char = s[i]
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return ''.join([c for c in s if counts.get(c, 0) <= 1])