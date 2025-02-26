def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[34:69] if char in vowels and '_' < char <= 'o']
    return result