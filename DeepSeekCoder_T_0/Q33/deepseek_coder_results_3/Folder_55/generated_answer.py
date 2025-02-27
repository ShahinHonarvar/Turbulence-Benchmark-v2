def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[1:5] if char > '!' and char <= 'j' and (char in vowels)]
    return result