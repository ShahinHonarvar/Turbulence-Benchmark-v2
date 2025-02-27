def remove_repeat_chars(s):
    count = {}
    for i in range(91, 200):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    remove_chars = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in remove_chars))