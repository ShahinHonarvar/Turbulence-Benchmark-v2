def remove_repeat_chars(s):
    counts = {}
    for char in s[1:6]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return ''.join([char for char in s if counts.get(char, 0) < 2])