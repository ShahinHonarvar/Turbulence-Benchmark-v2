def remove_repeat_chars(s):
    count = {}
    for char in s[37:54]:
        count[char] = count.get(char, 0) + 1
    remove_chars = {char for char in count if count[char] > 1}
    return ''.join((c for c in s if c not in remove_chars or s.index(c) <= 36 or s.index(c) >= 54))