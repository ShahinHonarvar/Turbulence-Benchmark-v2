def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(62, 97):
        char_count[chr(i)] = 0
    result = ''
    for char in s:
        if char in char_count:
            char_count[char] += 1
            if char_count[char] == 1:
                result += char
    return result