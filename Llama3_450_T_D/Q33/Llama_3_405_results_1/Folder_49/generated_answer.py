def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for i, c in enumerate(s) if 10 <= i < 97 and c > 'R' and (c <= 'b') and (c in vowels)]
    return result