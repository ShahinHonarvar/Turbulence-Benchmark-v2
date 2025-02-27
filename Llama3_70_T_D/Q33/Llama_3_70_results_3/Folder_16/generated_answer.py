def return_vowels(string, c, d):
    vowels = 'aeiouAEIOU'
    return [char for char in string[133:306] if char in vowels and c < char <= d]