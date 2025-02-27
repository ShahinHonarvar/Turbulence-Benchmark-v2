def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[50:77] if c > '#' and c <= 'r' and (c in vowels)]
    return result