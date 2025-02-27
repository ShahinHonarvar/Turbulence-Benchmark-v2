def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in vowels if string[71:89].index(char) and string[71:89][char] > 9 and (string[71:89][char] <= 'P')] or []