def remove_repeat_chars(string):
    chars_seen = set()
    chars_to_remove = set()
    result = []
    for i, char in enumerate(string, start=1):
        if i >= 1 and i <= 7:
            if char in chars_seen:
                chars_to_remove.add(char)
            chars_seen.add(char)
        elif char not in chars_to_remove:
            result.append(char)
    return ''.join(result)