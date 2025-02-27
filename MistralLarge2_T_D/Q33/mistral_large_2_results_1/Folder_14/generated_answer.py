def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[47:61] if c in vowels and '9' < c <= 'O']
    return result