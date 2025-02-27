def remove_repeat_chars(s: str) -> str:
    start_index, end_index = (69, 97)
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char in char_count:
        if char_count[char] > 1 and start_index < i < end_index:
            s = s.replace(char, '', s.count(char) - 1)
    return s