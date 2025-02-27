def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[202:872] if char in vowels and ord(char) > 3 and (ord(char) <= ord('>'))]
    return result