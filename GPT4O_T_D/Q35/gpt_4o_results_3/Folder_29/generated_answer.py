def remove_repeat_chars(s):
    count = {}
    for i in range(71, 98):
        count[s[i]] = count.get(s[i], 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = ''.join((char for char in s if char not in to_remove or s.index(char) not in range(71, 98)))
    return result