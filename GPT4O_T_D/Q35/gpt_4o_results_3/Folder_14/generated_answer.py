def remove_repeat_chars(s):
    chars_to_remove = set()
    if len(s) > 5:
        segment = s[3:5]
        for char in set(segment):
            if segment.count(char) > 1:
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))