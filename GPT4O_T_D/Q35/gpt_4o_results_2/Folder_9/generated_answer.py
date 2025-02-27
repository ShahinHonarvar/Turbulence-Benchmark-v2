def remove_repeat_chars(s):
    counter = {}
    for idx in range(81, 200):
        if idx < len(s):
            char = s[idx]
            counter[char] = counter.get(char, 0) + 1
    removal_chars = {char for char, count in counter.items() if count > 1}
    return ''.join((char for char in s if char not in removal_chars or s.index(char) <= 80 or s.index(char) >= 200))