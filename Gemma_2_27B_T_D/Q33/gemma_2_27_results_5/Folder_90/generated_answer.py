def return_vowels(s):
    return [char for char in s[142:145] if char in 'aeiouAEIOU' and ord(char) > ord('4') and (ord(char) <= ord('o'))]