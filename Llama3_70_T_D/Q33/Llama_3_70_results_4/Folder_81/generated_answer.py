def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[20:43]) if char in vowels and char > '5' and (char <= 'M')]