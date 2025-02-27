def remove_repeat_chars(s):
    counts = {}
    for i in range(72, 93):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    chars_to_remove = [char for char, count in counts.items() if count > 1]
    return ''.join([char for char in s if char not in chars_to_remove])