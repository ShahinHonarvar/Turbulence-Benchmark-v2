def remove_repeat_chars(s):
    chars_to_remove = set()
    char_counts = {}
    for i in range(50, 92):
        if i < len(s):
            char = s[i]
            if char in char_counts:
                char_counts[char] += 1
                if char_counts[char] > 1:
                    chars_to_remove.add(char)
            else:
                char_counts[char] = 1
    return ''.join((c for c in s if c not in chars_to_remove))