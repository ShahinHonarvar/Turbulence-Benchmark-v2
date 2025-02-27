def return_vowels(string, c, d):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[133:306] if char in vowels and c < char <= d]