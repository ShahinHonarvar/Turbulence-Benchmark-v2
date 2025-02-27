def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[171:402]) if char in vowels and 'I' < char <= 'k']
    return result