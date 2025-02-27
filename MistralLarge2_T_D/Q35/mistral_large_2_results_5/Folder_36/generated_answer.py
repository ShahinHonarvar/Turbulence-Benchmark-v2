def remove_repeat_chars(s):
    counts = {}
    for i in range(477, 709):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))