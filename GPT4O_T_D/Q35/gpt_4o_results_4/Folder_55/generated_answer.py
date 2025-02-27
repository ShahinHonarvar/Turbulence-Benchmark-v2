def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    middle_section = s[11:100] if len(s) > 100 else s[11:]
    count = {}
    for char in middle_section:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    to_remove = {char for char, c in count.items() if c > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 10 or s.index(char) >= 100))