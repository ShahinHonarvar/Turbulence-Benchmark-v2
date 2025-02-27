def remove_repeat_chars(string):
    char_occurrences = {}
    for char in string[27:96]:
        if char not in char_occurrences:
            char_occurrences[char] = 1
        else:
            char_occurrences[char] += 1
    altered_string = ''
    for char in string:
        if char_occurrences.get(char, 0) == 1:
            altered_string += char
    return altered_string