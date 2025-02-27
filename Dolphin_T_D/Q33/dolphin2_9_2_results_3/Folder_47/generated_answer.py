def return_vowels(text, n, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[23:38] if n < char <= k and char in vowels]