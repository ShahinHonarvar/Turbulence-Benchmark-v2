def remove_repeat_chars(s):
    count = {}
    for i in range(1, 6):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 0 or s.index(char) >= 6))