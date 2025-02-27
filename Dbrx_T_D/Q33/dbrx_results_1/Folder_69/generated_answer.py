def return_vowels(char_string):
    vowels = []
    for char in char_string[641:872]:
        if char.lower() > '>' and char.lower() <= 'q' and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels