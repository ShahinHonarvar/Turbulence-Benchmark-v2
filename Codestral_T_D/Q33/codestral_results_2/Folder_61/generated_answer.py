def return_vowels(string):
    return [char for char in string[1:4] if char in 'AEIOU' and 'C' < char <= 'I']