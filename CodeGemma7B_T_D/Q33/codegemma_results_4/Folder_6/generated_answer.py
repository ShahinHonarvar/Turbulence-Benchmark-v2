def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in str[20:34] if letter in vowels and letter > 'U' and (letter <= 'i')] or []