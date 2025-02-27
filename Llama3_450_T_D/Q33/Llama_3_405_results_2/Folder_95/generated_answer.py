def return_vowels(s):
    vowels = 'AEIO'
    return [char for i, char in enumerate(s[32:61]) if char in vowels and '?' < char <= 'P']