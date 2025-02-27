def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[44:95] if char in vowels and ord(char) > 53 and (ord(char) <= 76)]
    return result