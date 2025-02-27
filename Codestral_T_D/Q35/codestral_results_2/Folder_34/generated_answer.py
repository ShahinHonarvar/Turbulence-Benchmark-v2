def remove_repeat_chars(s):
    char_count = {}
    for i in range(70, 200):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    new_string = ''
    for char in s:
        if char_count.get(char, 0) <= 1:
            new_string += char
    return new_string