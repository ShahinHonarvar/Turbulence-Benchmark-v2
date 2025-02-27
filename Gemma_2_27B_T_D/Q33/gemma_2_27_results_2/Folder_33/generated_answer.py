def return_vowels(string):
    return [letter for letter in string[163:771] if letter in 'aeiouAEIOU' and letter > ':' and (letter <= 'E')]