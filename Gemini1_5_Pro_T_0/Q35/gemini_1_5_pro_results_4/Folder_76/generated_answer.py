def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 330 < i < 543:
            if char in seen_chars:
                continue
            else:
                if s.count(char) > 1:
                    seen_chars.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)