def remove_repeat_chars(s):
    counts = {}
    for i in range(18, 60):
        if 0 <= i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    repeat_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))