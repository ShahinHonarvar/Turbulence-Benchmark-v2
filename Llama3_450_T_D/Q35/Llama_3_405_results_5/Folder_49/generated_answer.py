def remove_repeat_chars(s):
    char_count = {}
    for i in range(90, 200):
        try:
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
        except IndexError:
            break
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join([char for char in s if char not in repeat_chars])