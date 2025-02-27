def return_vowels(string):
    vowels = []
    for i in range(10, 97):
        character = string[i]
        if character > 'R' and character <= 'b':
            vowels.append(character)
    return vowels