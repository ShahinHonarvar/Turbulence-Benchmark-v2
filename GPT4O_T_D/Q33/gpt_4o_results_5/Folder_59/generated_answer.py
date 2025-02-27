def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[8:9] if char in vowels and char > 'Y' and (char <= 's')]