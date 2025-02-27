def filter_chars(s):
    if len(s) < 80:
        section_of_interest = s[36:80]
    else:
        section_of_interest = s[36:80]
    chars_to_remove = set((c for c in section_of_interest if '2' <= c <= 's'))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result