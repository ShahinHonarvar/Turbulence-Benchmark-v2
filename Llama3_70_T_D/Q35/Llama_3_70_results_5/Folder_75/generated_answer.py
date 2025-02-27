def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = set()
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.add(char)
    for i in range(20, 51):
        if s[i] in repeat_chars:
            repeat_chars.remove(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result