def return_vowels(string):
    vowels_to_check = string[24:59]
    vowels = [char for char in vowels_to_check if char in 'aeiouAEIOU' and ord(char) > ord('N') and (ord(char) <= ord('U'))]
    return vowels