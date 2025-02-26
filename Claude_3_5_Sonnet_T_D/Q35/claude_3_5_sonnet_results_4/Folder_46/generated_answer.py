def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    end = min(79, len(s))
    section = s[11:end]
    chars_to_remove = set((c for c in section if section.count(c) > 1))
    result = s[:11] + ''.join((c for c in section if c not in chars_to_remove))
    if end < len(s):
        result += s[end:]
    return result