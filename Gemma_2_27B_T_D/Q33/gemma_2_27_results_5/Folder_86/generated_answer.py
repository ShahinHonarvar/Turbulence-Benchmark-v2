def return_vowels(s):
    return [c for c in s[273:275] if ord(c) > ord('+') and ord(c) <= ord('o') and (c in 'aeiouAEIOU')]