def return_vowels(string):
    return [char for char in string[202:872] if char in 'aeiouAEIOU' and ord(char) > 3 and (ord(char) <= ord('>'))]