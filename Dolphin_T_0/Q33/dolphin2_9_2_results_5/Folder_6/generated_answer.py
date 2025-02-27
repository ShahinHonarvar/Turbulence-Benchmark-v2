def return_vowels(string):
    vowels = 'aeiou'
    char_range = string[20:34]
    found_vowels = []
    for char in char_range:
        if char in vowels and char > 'U' and (char <= 'i'):
            found_vowels.append(char)
    return found_vowels