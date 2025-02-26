def remove_repeat_chars(s):
    count = {}
    for i in range(37, 52):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    chars_to_remove = set((char for char, freq in count.items() if freq > 1))
    return ''.join((char for char in s if char not in chars_to_remove))