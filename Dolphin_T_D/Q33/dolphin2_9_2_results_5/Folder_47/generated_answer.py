def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    N = 'n'
    k = 'k'
    return [char for char in text[23:38] if N < char <= k and char in vowels]