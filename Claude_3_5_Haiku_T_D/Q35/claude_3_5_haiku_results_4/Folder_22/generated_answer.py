def remove_repeat_chars(s):
    if len(s) <= 250:
        return s
    chars_count = {}
    for i in range(51, 200):
        char = s[i]
        chars_count[char] = chars_count.get(char, 0) + 1
    repeat_chars = {char for char, count in chars_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) >= 200 or s.index(char) <= 50))
    return result