def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [letter for letter in vowels if 10 <= string.index(letter) < 82 and string[string.index(letter)] > '$' and (string[string.index(letter)] <= '@')]