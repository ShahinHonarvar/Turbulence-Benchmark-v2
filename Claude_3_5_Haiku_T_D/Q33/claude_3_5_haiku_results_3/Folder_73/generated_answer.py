def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[47:89] if char in vowels and ord(char) > ord('@') and (ord(char) <= ord('n'))]
    return result