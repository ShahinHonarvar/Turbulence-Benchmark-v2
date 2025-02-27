def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if i > 17 and i < 60:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    repeat_chars = [char for char in char_count if char_count[char] > 1]
    return ''.join([char for char in s if char not in repeat_chars])