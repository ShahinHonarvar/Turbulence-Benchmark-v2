def remove_repeat_chars(s):
    char_count = {}
    for i in range(10, 80):
        if i < len(s):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    return ''.join([char for char in s if char_count.get(char, 0) <= 1])