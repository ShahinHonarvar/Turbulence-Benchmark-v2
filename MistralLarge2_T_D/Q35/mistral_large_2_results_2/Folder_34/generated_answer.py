def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s):
        if 70 < i < 200:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''.join([char for char in s if char_count.get(char, 0) < 2])
    return result