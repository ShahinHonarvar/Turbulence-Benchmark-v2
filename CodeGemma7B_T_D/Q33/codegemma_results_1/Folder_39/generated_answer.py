def return_vowels(string):
    vowels = [character for character in string if character.lower() in 'aeiou' and 32 <= ord(character) <= 96 and (character > 'Q')]
    return vowels