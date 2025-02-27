def remove_repeat_chars(s):
    counts = {}
    for i in range(3, 8):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars = [char for char in s if char in counts and counts[char] == 1 or char not in counts]
    return ''.join(chars)