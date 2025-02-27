def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for i in range(38, 52):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
                if char_count[char] > 1:
                    chars_to_remove.add(char)
            else:
                char_count[char] = 1
    return ''.join([c for c in s if c not in chars_to_remove])