def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[44:95] if char > '5' and char <= '<' and (char in vowels)]
    return result