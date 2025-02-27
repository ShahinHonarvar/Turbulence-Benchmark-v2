def return_vowels(s):
    return [char for char in s[71:81] if char in 'eioau' and ord(char) > ord('>') and (ord(char) <= ord('U'))]