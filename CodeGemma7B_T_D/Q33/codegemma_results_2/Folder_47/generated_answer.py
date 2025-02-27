def return_vowels(string):
    return [letter for letter in string[23:38] if letter in 'aeiouAEIOU' and letter > 'N' and (letter <= 'k')]