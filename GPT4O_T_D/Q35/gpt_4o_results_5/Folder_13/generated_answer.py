def remove_repeat_chars(s):
    substring = s[47:91]
    seen = set()
    to_remove = set()
    for char in substring:
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in to_remove or not 47 <= s.index(char) < 91))