def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [letter for letter in string[22:82] if letter in vowels and letter > 'N' and (letter <= 'o')]