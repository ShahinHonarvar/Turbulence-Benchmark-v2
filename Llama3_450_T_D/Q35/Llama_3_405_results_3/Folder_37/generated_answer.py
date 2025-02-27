def remove_repeat_chars(s):
    count = {}
    for i in range(2, 7):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    chars_to_remove = [char for char, freq in count.items() if freq > 1]
    return ''.join([char for char in s if char not in chars_to_remove])