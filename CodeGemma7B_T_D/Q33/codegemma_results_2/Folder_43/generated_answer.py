def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowels = []
    for i, char in enumerate(string):
        if i >= 22 and i < 82 and (char.lower() in vowels) and (char > 'N') and (char <= 'o'):
            found_vowels.append(char.lower())
    return found_vowels