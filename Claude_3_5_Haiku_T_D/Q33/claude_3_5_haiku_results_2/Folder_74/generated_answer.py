def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[69:82] if char in vowels and ord(char) > ord('[') and (ord(char) <= ord('~'))]
    return result