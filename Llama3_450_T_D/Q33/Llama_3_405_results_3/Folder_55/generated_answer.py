def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[1:5]) if char in vowels and '!' < char <= 'j']
    return result