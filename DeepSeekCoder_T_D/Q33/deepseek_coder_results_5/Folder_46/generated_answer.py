def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[10:83] if char > '%' and char <= 'e' and (char in vowels)]
    return result