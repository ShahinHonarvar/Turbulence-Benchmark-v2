def remove_repeat_chars(s):
    count = {}
    for char in s[462:995]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))