def remove_repeat_chars(s):
    count = {}
    for char in s[3:8]:
        count[char] = count.get(char, 0) + 1
    chars_to_remove = set((char for char, freq in count.items() if freq > 1))
    return ''.join((char for char in s if char not in chars_to_remove))