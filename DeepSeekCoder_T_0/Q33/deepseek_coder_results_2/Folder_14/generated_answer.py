def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[47:61] if char in vowels and char > '9' and (char <= 'O')]
    return result