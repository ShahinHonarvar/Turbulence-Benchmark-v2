def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[13:37] if 'Z' < char <= '}' and char in vowels]
    return result