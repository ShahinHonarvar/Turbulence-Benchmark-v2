def remove_repeat_chars(s):
    counts = {}
    for char in s[2:8]:
        counts[char] = counts.get(char, 0) + 1
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))