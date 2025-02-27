def remove_repeat_chars(s: str) -> str:
    start, end = (51, 76)
    char_count = {}
    for i, char in enumerate(s):
        if start <= i < end:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        elif i >= end:
            break
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s