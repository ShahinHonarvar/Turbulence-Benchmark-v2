def remove_repeat_chars(s):
    count = {}
    for i in range(35, 64):
        if i >= len(s):
            break
        count[s[i]] = count.get(s[i], 0) + 1
    return ''.join((char for char in s if count.get(char, 0) <= 1))