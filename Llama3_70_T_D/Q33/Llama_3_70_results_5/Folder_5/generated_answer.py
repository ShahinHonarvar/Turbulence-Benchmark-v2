def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s) if 44 <= i < 95 and c > chr(5) and (c <= '<') and (c in vowels)]