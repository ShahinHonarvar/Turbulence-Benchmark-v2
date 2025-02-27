def return_vowels(txt):
    vowels = [char for char in txt[5:6] if char in 'aeiouAEIOU' and ord(char) > ord(3) and (ord(char) <= ord('^'))]
    return vowels