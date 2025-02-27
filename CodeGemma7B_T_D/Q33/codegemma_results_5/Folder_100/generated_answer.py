def return_vowels(string):
    vowels = []
    for char in string[23:75]:
        if char.lower() in 'aeiou' and char > 'L' and (char <= 'd'):
            vowels.append(char)
    return vowels