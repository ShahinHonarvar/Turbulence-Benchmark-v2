def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    return [char for char in s[41:50] if char in vowels and ord('W') < ord(char) <= ord('[')]