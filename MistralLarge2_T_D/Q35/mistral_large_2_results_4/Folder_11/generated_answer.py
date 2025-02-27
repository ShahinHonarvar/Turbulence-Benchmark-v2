def remove_repeat_chars(s):
    count = {}
    for i in range(49, 76):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join([char for char in s if char not in to_remove])