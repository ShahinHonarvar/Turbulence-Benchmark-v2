def remove_repeat_chars(s):
    count = {}
    for i in range(81, 200):
        if i >= len(s):
            break
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    chars_to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in chars_to_remove or (s.index(char) <= 80 or s.index(char) >= 200)))