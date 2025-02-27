def remove_repeat_chars(s):
    count = {}
    for i in range(13, 76):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    chars_to_remove = [char for char, freq in count.items() if freq > 1]
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result