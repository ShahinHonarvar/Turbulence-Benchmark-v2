def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[21:59] if char > '/' and char <= 'a' and (char in vowels)]
    return result