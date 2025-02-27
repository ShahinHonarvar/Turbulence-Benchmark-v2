def return_vowels(string):
    vowels = []
    for character in string[260:322]:
        if 'a' <= character <= 'u' and character % 128 > 37 and (character <= 85):
            vowels.append(character)
    return vowels