def return_vowels(string):
    vowels = []
    for char in string[40:94]:
        if char > '4' and char <= 'H':
            if char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels