def remove_repeat_chars(s):
    middle_section = s[87:90]
    repeated_chars = set((c for c in middle_section if middle_section.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars or s.index(c) < 87 or s.index(c) >= 90))