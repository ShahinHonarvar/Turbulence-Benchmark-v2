def remove_repeat_chars(s):
    substring = s[38:81]
    count = {}
    for char in substring:
        count[char] = count.get(char, 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))