def remove_repeat_chars(s):
    if len(s) <= 355:
        return s
    count = {}
    for char in s[356:988]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 355 or s.index(char) >= 988))