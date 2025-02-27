def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[51:77] if char in vowels and char > chr(4) and (char <= chr(61))]