def return_vowels(s, n, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[23:38] if n < ch <= k and ch in vowels]
    return result