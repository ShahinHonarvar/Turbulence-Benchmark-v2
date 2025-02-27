def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[71:88] if char in vowels and '9' < char <= 'P']
    return result