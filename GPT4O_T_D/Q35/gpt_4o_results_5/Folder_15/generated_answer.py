def remove_repeat_chars(s):
    repeated_chars = set()
    middle_section = s[1:4]
    for char in middle_section:
        if middle_section.count(char) > 1:
            repeated_chars.add(char)
    return ''.join((char for char in s if char not in repeated_chars))