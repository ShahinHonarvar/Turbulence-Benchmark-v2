def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[22:82] if char in vowels and char > 'N' and (char <= 'o')]