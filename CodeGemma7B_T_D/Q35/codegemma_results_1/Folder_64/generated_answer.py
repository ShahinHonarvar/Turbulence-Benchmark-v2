def remove_repeat_chars(str1):
    seen = set()
    RESULT = str()
    for char in str1:
        if char not in seen and 0 < len(str1) <= 5:
            seen.add(char)
            RESULT += char
    return RESULT.strip()