def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[71:88] if c > chr(9) and ord(c) <= ord('P') and (c in vowels)]