def remove_repeat_chars(s):
    count = {}
    for i in range(13, 76):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    to_remove = {char for char, freq in count.items() if freq > 1}
    return ''.join((char for char in s if char not in to_remove))