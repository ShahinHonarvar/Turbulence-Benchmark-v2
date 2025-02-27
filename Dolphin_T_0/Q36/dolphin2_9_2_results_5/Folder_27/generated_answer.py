def filter_chars(s):
    chars_to_remove = [s[i] for i in range(48, 75) if '6' < s[i] < '_']
    chars_to_remove = list(set(chars_to_remove))
    altered_string = ''
    for i in s:
        if i not in chars_to_remove:
            altered_string += i
    return altered_string