def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[142:145] if char in vowels and char > '4' and (char <= 'o')]