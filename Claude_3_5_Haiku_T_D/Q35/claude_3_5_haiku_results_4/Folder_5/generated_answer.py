def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    segment = s[3:-1]
    to_remove = set()
    for char in segment:
        if segment.count(char) > 1 and char not in to_remove:
            to_remove.add(char)
    result = s[0:3] + ''.join((char for char in segment if char not in to_remove)) + s[-1]
    return result