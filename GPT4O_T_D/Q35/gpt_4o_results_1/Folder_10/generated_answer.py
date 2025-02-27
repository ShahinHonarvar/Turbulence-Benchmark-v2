def remove_repeat_chars(s):
    count = {}
    for char in s[37:54]:
        count[char] = count.get(char, 0) + 1
    to_remove = {char for char, c in count.items() if c > 1}
    return ''.join((char for char in s if char not in to_remove or not 37 <= s.index(char) < 54))