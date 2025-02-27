def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s if char in vowels and 'P' < char <= 'z' and (ord('A') <= ord(char) < ord('R'))]
    return result