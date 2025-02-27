def remove_repeat_chars(s):
    if len(s) <= 7:
        return s
    mid_section = s[7:9]
    duplicates = {char for char in mid_section if mid_section.count(char) > 1}
    return ''.join((char for char in s if char not in duplicates))