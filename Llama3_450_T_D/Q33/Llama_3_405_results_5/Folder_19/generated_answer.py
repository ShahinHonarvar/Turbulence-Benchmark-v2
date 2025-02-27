def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[51:77] if c in vowels and chr(4) < c <= chr(ord('='))]
    return result