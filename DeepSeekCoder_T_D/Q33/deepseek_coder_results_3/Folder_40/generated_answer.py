def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[2:7] if char > '^' and char <= 'd' and (char in vowels)]
    return result