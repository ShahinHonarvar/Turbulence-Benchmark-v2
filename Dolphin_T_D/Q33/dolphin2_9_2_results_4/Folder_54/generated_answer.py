def return_vowels(some_string):
    English_vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_found = []
    for character in some_string[23:85]:
        if character >= 'W' and character <= 'v':
            if character.lower() in English_vowels:
                vowels_found.append(character)
    return vowels_found