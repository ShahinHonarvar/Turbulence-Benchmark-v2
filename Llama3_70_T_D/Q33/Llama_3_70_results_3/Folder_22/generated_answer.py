def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[56:90], 56) if char in vowels and char > 'K' and (char <= 'z')]