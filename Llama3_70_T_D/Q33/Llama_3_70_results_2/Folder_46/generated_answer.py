def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[10:84]) if char > '%' and char <= 'e' and (char in vowels)]