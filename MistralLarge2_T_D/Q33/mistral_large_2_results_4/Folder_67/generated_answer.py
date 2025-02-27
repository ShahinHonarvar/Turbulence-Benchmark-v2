def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[21:59] if char in vowels and '/' < char <= 'a']