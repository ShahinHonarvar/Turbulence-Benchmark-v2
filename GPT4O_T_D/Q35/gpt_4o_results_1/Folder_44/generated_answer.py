def remove_repeat_chars(s):
    counts = {}
    for char in s[37:52]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    characters_to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in characters_to_remove or s.index(char) <= 36 or s.index(char) >= 52))