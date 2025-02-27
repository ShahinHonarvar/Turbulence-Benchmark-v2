def remove_repeat_chars(string):
    seen_chars = set()
    new_string = ''
    for i, char in enumerate(string):
        if not 103 <= i <= 801 or char in seen_chars:
            continue
        seen_chars.add(char)
        new_string += char
    return new_string