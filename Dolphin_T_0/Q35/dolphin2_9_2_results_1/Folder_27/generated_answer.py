def remove_repeat_chars(input_characters):
    char_occurrences = {}
    for char in input_characters:
        if 86 <= input_characters.index(char) < 89 and input_characters.count(char) > 1:
            char_occurrences[char] = input_characters.count(char)
    for char, count in char_occurrences.items():
        input_characters = input_characters.replace(char, '')
    return input_characters