def remove_repeat_chars(s):
    """Remove repeating characters between indices 42 and 55"""
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 42 < i < 55:
            if c not in seen:
                seen.add(c)
                result.append(c)
    return ''.join(result)