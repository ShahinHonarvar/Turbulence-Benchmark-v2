def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 1 <= i < 9 and '?' < c <= 'k' and (c in vowels)]