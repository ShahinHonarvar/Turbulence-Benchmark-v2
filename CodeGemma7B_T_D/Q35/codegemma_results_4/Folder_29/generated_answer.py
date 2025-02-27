def remove_repeat_chars(s):
    seen_characters = set()
    new_string = ''
    for i, char in enumerate(s):
        if 70 < i < 98 and char not in seen_characters:
            seen_characters.add(char)
            new_string += char
    return new_string