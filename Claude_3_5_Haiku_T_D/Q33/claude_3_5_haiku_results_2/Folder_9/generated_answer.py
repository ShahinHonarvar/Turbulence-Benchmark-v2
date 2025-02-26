def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[13:35] if char in vowels and ord(char) > ord('8') and (ord(char) <= ord('F'))]
    return result