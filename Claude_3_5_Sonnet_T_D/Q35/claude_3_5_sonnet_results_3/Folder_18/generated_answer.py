def remove_repeat_chars(s):
    count = {}
    for i in range(57, 90):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    chars_to_remove = set((char for char, freq in count.items() if freq > 1))
    return ''.join((char for char in s if char not in chars_to_remove))