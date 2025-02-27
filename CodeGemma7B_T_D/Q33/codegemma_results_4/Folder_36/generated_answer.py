def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for letter in string[604:949]:
        if letter in vowels and letter > 'N' and (letter <= 'U'):
            filtered_vowels.append(letter)
    return filtered_vowels