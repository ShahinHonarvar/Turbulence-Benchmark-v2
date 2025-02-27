def remove_repeat_chars(s):
    count = {}
    for i in range(11, min(79, len(s))):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    chars_to_remove = {char for char, c in count.items() if c > 1}
    return ''.join((char for char in s if char not in chars_to_remove))