def remove_repeat_chars(s):
    mid_section = s[35:69]
    count = {}
    for char in mid_section:
        count[char] = count.get(char, 0) + 1
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) not in range(35, 69)))