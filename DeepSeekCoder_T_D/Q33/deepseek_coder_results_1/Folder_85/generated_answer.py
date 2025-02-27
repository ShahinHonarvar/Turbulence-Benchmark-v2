def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[55:65] if char > 'Z' and char <= 'w' and (char in vowels)]
    return result