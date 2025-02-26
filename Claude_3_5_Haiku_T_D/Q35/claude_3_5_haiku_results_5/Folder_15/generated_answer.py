def remove_repeat_chars(s):
    if len(s) <= 5:
        return s
    first_five = s[1:5]
    chars_to_remove = set((char for char in first_five if first_five.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))