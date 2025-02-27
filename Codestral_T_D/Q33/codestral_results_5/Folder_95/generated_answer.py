def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[32:61] if '?' < char <= 'P' and char in vowels]