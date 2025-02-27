def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[64:82] if char > 'P' and char <= 'z' and (char in vowels)]
    return result