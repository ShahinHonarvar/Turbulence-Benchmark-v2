def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for idx, ch in enumerate(s[529:828]) if ch in vowels and 'U' < ch <= 'l']
    return result