def remove_repeat_chars(s):
    count = {}
    for i in range(476, 709):
        if i >= len(s):
            break
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = {char for char, freq in count.items() if freq > 1}
    return ''.join([char for char in s if char not in repeat_chars])