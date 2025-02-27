def return_vowels(s):
    vowels = [char for char in s[273:275] if char > '+' and char <= 'o']
    return [char for char in vowels if char in 'aeiou']