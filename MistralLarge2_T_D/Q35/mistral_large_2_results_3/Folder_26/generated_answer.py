def remove_repeat_chars(s):
    count = {}
    for i in range(68, 99):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    remove_chars = {char for char, freq in count.items() if freq > 1}
    return ''.join((char for char in s if char not in remove_chars))