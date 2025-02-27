def remove_repeat_chars(s: str) -> str:
    chars_between_36_and_52 = set(s[36:52])
    seen_chars = set()
    result = []
    for char in s:
        if 36 <= s.index(char) < 52:
            if char in chars_between_36_and_52 and char not in seen_chars:
                seen_chars.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)