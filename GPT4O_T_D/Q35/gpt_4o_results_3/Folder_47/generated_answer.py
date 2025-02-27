def remove_repeat_chars(s):
    substring = s[30:53]
    count = {}
    for char in substring:
        count[char] = count.get(char, 0) + 1
    chars_to_remove = {char for char, c in count.items() if c > 1}
    return ''.join((char for char in s if char not in chars_to_remove or (s.index(char) < 30 or s.index(char) > 52)))