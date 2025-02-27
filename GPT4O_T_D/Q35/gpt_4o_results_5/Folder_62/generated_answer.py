def remove_repeat_chars(s):
    if len(s) <= 50:
        return s
    count = {}
    subsection = s[51:92]
    for char in subsection:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    chars_to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result