def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 1 < i < 8 and char in s[2:i]:
            if char not in seen_chars:
                seen_chars.add(char)
                result = result[:result.rfind(char)]
        else:
            result += char
    return result