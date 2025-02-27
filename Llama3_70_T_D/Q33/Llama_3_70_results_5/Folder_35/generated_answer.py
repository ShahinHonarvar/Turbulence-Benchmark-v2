def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[483:664] if char > '&' and char <= 'h' and (char in vowels)]
    return result