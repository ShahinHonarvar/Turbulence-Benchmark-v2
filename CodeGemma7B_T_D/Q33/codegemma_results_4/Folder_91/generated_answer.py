def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in vowels if string[4:8].lower().startswith(letter) and letter >= 'p' and (letter <= 'r')]