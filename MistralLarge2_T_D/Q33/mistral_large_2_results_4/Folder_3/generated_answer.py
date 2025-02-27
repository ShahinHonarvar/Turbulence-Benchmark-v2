def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for i, ch in enumerate(s) if 50 <= i < 77 and '#' < ch <= 'r' and (ch in vowels)]
    return result