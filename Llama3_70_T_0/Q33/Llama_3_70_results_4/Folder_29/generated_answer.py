def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[19:20] if char in vowels and char > '<' and (char <= 'p')]