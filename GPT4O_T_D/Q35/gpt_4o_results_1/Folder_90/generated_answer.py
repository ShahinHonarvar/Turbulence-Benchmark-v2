def remove_repeat_chars(s):
    mid_section = s[307:807]
    repeat_chars = {c for c in mid_section if mid_section.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) <= 306 or s.index(c) >= 807))