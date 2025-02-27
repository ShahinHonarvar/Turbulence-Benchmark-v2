def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [letter for letter in vowels if letter in word and letter > 'W' and (letter <= 'v') and (23 <= word.index(letter) < 85)]