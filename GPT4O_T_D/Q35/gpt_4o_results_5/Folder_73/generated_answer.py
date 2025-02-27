def remove_repeat_chars(s):
    count = {}
    for i in range(11, 76):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 10 or s.index(char) >= 76))