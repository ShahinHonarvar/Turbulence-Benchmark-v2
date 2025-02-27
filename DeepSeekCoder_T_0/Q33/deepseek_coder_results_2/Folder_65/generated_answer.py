def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[71:88] if char in vowels and ord(char) > 57 and (ord(char) <= 80)]
    return result