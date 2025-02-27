def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[32:61] if char > '?' and char <= 'P' and (char in vowels)]
    return result