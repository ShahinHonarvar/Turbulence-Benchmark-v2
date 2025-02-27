def return_vowels(string):
    return [letter for letter in string[22:82] if letter in 'aeiouAEIOU' and letter > 'N' and (letter <= 'o')]