def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[71:88] if char in vowels and ord('9') < ord(char) <= ord('P')]
    return result