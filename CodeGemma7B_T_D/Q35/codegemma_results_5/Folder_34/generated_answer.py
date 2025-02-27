def remove_repeat_chars(string):
    seen_chars = set()
    new_string = []
    for char in string:
        if char not in seen_chars and 70 < string.index(char) < 200:
            seen_chars.add(char)
            new_string.append(char)
    return ''.join(new_string)