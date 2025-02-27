def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[202:872] if char in vowels and 3 < ord(char) <= ord('>')]