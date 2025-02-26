def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    target_section = s[87:89]
    repeat_chars = set((char for char in target_section if target_section.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))