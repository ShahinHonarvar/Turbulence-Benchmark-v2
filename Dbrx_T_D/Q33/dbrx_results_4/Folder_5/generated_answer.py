def return_vowels(string):
    vowels = []
    for char in string[44:95]:
        if char > '5' and char <= '<' and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels