def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 22 <= i < 82 and c > 'N' and (c <= 'o') and (c in vowels)]