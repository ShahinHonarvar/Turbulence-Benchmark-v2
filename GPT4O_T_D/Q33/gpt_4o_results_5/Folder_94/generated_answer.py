def return_vowels(s):
    vowels = set('AEIOUaeiou')
    return [ch for ch in s[40:94] if ch in vowels and '4' < ch <= 'H']