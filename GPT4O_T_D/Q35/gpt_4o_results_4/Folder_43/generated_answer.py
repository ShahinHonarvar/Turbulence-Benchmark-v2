def remove_repeat_chars(s):
    sub_s = s[11:28]
    count = {}
    for char in sub_s:
        count[char] = count.get(char, 0) + 1
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 10 or s.index(char) >= 28))