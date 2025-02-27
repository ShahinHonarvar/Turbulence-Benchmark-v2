def remove_repeat_chars(s):
    counts = {}
    for i, char in enumerate(s):
        if 1 < i < 8:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    result = ''.join((char for char in s if counts.get(char, 0) < 2))
    return result