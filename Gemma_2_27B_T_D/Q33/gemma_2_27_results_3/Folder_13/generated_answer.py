def return_vowels(text):
    return [letter for letter in text[149:313] if letter in 'aeiouAEIOU' and letter > 'M' and (letter <= 'j')]