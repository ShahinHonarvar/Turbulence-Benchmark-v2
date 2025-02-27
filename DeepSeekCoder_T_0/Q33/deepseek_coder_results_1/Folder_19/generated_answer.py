def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[51:77] if char in vowels and ord('4') < ord(char) <= ord('=')]
    return result