def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[27:57] if char in vowels and 'o' < char <= 'w']
    return result