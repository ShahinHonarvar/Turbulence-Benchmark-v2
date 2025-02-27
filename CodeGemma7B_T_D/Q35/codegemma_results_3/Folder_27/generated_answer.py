def remove_repeat_chars(text):
    repeated_letters = set()
    new_text = ''
    for i, char in enumerate(text):
        if i >= 86 and i <= 89 and (char in repeated_letters):
            continue
        elif i >= 86 and i <= 89:
            repeated_letters.add(char)
        new_text += char
    return new_text