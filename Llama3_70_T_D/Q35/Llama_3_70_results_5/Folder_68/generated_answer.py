def remove_repeat_chars(s):
    char_count = {}
    for i in range(10, len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    for i in range(10):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    repeat_chars = set()
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])